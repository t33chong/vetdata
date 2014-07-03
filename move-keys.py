from boto import connect_s3
from uuid import uuid4

conn = connect_s3()
bucket = conn.get_bucket('nlp-data')

keys = bucket.list('data_events_processing/')

for key in keys:
    new = 'data_events/%s' % str(uuid4())
    print key.key, new
    key.copy('nlp-data', new)
    key.delete()
