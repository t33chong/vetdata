import os
import sys
import json
import gzip
import logging
from multiprocessing import Pool
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from WikiaSolr import QueryIterator
from nlp_client import title_confirmation
from nlp_client.services import AllTitlesService

title_confirmation.USE_S3 = False

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('dump-titles.log')
fh.setLevel(logging.ERROR)
logger.addHandler(fh)

docs = [wid.strip() for wid in open('missing-titles.txt')]

titles_dir = '/data/titles/'

bucket = S3Connection().get_bucket('nlp-data')
k = Key(bucket)

def call_titles(doc):
    try:
        logger.debug('Calling AllTitlesService on %s' % doc)
        titles = json.dumps(AllTitlesService().get(doc), ensure_ascii=False)
        titles_file = titles_dir + doc + '.gz'
        g = gzip.GzipFile(titles_file, 'w')
        g.write(titles)
        g.close()
        k.key = 'article_titles/%s' % os.path.basename(titles_file)
        k.set_contents_from_filename(titles_file)
        os.remove(titles_file)
    except Exception as e:
        logger.error('FAILED! %s ~ %s ~ %s' % (doc, type(e).__name__, e))
        #raise

pool = Pool(processes=4)
pool.map(call_titles, docs)
