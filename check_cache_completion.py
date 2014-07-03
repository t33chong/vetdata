from boto.s3.connection import S3Connection
from boto.s3.key import Key
#from boto.utils import get_instance_metadata
from collections import defaultdict

bucket = S3Connection().get_bucket('nlp-data')

hostnames = ['ip-10-238-9-25.us-west-2.compute.internal',
             'ip-10-238-3-181.us-west-2.compute.internal',
             'ip-10-253-2-34.us-west-2.compute.internal',
             'ip-10-235-0-83.us-west-2.compute.internal',
             'ip-10-231-139-117.us-west-2.compute.internal']

d = defaultdict(int)

def is_valid(key):
    for hostname in hostnames:
        if hostname in key:
            d[hostname] += 1
            return True
    return False

#keys = filter(is_valid, bucket.list('data_processing/'))
#
#print keys

count = 0
for key in bucket.list('data_processing/'):
    if is_valid(key.key):
        count += 1
        print key.key

print count
for hostname in d:
    print hostname, d[hostname]
