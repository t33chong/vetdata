import os
import uuid
import shutil
import tarfile
import logging
from boto.s3.connection import S3Connection
from boto.s3.key import Key

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
fh = logging.FileHandler('reupload.log')
fh.setLevel(logging.ERROR)
logger.addHandler(sh)
logger.addHandler(fh)

bucket = S3Connection().get_bucket('nlp-data')
k = Key(bucket)

def get_events():
    text_events = bucket.list(prefix='text_events/')
    for text_event in text_events:
        if text_event.name.endswith('.tgz'):
            if len(os.path.basename(text_event.name)) < 20:
                yield text_event.name

batch_count = 0
id_ = str(uuid.uuid4())

for text_event in get_events():
    text_dir = '/home/ubuntu/text_files/%s' % id_
    # get .tgz file from s3
    local_file = '/home/ubuntu/text_events/' + os.path.basename(text_event)
    k.key = text_event
    try:
        logger.debug('Getting %s' % local_file)
        k.get_contents_to_filename(local_file)
        k.delete()
        # untar in ~/text_files
        untar = tarfile.open(local_file)
        untar.extractall(text_dir)
        untar.close()
    except Exception as e:
        logger.error('Error: %s - %s - %s' % (local_file, type(e).__name__, e))
        continue
    # if # of files is at least 500, add to new tar
    if len(os.listdir(text_dir)) >= 500:
        tarname = '/home/ubuntu/new_tarballs/%s.tgz' % id_
        logger.debug('file count: %i - adding to %s' % (len(os.listdir(text_dir)), tarname))
        tar = tarfile.open(tarname, 'w:gz')
        tar.add(text_dir, '.')
        tar.close()
        batch_count += 1
        id_ = str(uuid.uuid4())
        # move to s3
        k.key = 'text_events/%s' % os.path.basename(tarname)
        k.set_contents_from_filename(tarname)
        # clean up
        os.remove(tarname)
        shutil.rmtree(text_dir)
