from boto.s3.connection import S3Connection
from boto.s3.key import Key

bucket = S3Connection().get_bucket('nlp-data')
keys = filter(lambda x: x.key.endswith('.xml'), bucket.list('xml/831/'))
k = Key(bucket)

print len(keys)

for n in range(0, len(keys), 500):
    event_string = '\n'.join([key.key for key in keys[n:n+500]])
    k.key = 'data_events/%d' % n
    k.set_contents_from_string(event_string)
    print 'writing to %s' % k.key
