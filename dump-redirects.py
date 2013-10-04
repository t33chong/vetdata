import os
import sys
import json
import gzip
from multiprocessing import Pool
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from WikiaSolr import QueryIterator
from nlp_client import title_confirmation
from nlp_client.services import RedirectsService

title_confirmation.USE_S3 = False

docs = [wid.strip() for wid in open('missing-redirects.txt')]

redirects_dir = '/data/redirects/'

bucket = S3Connection().get_bucket('nlp-data')
k = Key(bucket)

def call_redirects(doc):
    try:
        print 'Calling RedirectsService on', doc
        redirects = json.dumps(RedirectsService().get(doc), ensure_ascii=False)
        redirects_file = redirects_dir + doc + '.gz'
        g = gzip.GzipFile(redirects_file, 'w')
        g.write(redirects)
        g.close()
        k.key = 'article_redirects/%s' % os.path.basename(redirects_file)
        k.set_contents_from_filename(redirects_file)
        os.remove(redirects_file)
    except:
        print doc, 'failed!'
        raise

pool = Pool(processes=7)
pool.map(call_redirects, docs)
