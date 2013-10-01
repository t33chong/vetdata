import os
import json
import gzip
from multiprocessing import Pool
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from WikiaSolr import QueryIterator
from nlp_client import title_confirmation
from nlp_client.services import RedirectsService

title_confirmation.USE_S3 = False

qi = QueryIterator('http://search-s10:8983/solr/xwiki/', {'query': 'lang_s:en', 'fields': 'id', 'sort': 'id asc'})

#def gen_docs():
#    for doc in qi:
#        print 'yielding', doc['id']
#        yield doc['id']
#
#docs = gen_docs()

docs = []
for doc in qi:
    print 'appending', doc['id']
    docs.append(doc['id'])


redirects_dir = '/data/redirects/'

bucket = S3Connection().get_bucket('nlp-data')
k = Key(bucket)

def call_redirects(doc):
    try:
        print 'Calling RedirectsService on', doc
        redirects = json.dumps(RedirectsService().get(doc))
        redirects_file = redirects_dir + doc + '.gz'
        g = gzip.GzipFile(redirects_file, 'w')
        g.write(redirects)
        g.close()
        k.key = 'article_redirects/%s' % os.path.basename(redirects_file)
        k.set_contents_from_filename(redirects_file)
        os.remove(redirects_file)
    except:
        print doc, 'failed!'

pool = Pool(processes=7)
pool.map(call_redirects, docs)
