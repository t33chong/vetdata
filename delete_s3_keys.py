from boto.s3.connection import S3Connection
from boto.s3.key import Key

bucket = S3Connection().get_bucket('nlp-data')
k = Key(bucket)

for line in open('all.errors'):
    wid = line.strip()
    k.key = 'xml/%s/' % wid
    k.delete()
    k.key = 'service_responses/%s/' % wid
    k.delete()
