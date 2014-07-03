from boto.s3.connection import S3Connection
from boto.s3.key import Key

bucket = S3Connection().get_bucket('nlp-data')
keys = filter(lambda x: not x.key.endswith('/'), bucket.list('data_processing_bak/'))

for key in keys:
    new = key.key.replace('data_processing_bak', 'data_events')
    print 'moving %s to %s' % (key.key, new)
    key.copy('nlp-data', new)
    key.delete()
