from boto.s3.connection import S3Connection
from boto.s3.key import Key

bucket = S3Connection().get_bucket('nlp-data')

count = 0
for key in bucket.list('service_responses/'):
    if key.key.endswith('WpDocumentEntitySentimentService.get'):
        count += 1
        print key.key

print count
