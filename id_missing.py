import re
from time import sleep
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from WikiaSolr import QueryIterator

bucket = S3Connection().get_bucket('nlp-data')

qi = QueryIterator('http://search-s10:8983/solr/xwiki/', {'query': 'lang_s:en', 'fields': 'id', 'sort': 'id asc'})

t = open('missing-titles.txt', 'w')
r = open('missing-redirects.txt', 'w')

for doc in qi:
    wid = doc['id']
    print 'checking', wid
    if not bucket.get_key('article_titles/%s.gz' % wid):
        print wid, 'missing from titles'
        t.write('%s\n' % wid)
    if not bucket.get_key('article_redirects/%s.gz' % wid):
        print wid, 'missing from redirects'
        r.write('%s\n' % wid)

t.close()
r.close()
