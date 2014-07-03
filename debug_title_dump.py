import re
from WikiaSolr import QueryIterator
from boto.s3.connection import S3Connection
from boto.s3.key import Key

qi = QueryIterator('http://search-s10:8983/solr/xwiki/', {'query': 'lang_s:en', 'fields': 'id', 'sort': 'wam_i desc', 'wt': 'json'})

bucket = S3Connection().get_bucket('nlp-data')

titles = {}
for key in bucket.list(prefix='article_titles/'):
    if key.name.endswith('gz'):
        wid = int(re.search('/([0-9]+)\.gz', key.name).group(1))
        print 'Adding %i to titles dict...' % wid
        titles[wid] = True

redirects = {}
for key in bucket.list(prefix='article_redirects/'):
    if key.name.endswith('gz'):
        wid = int(re.search('/([0-9]+)\.gz', key.name).group(1))
        print 'Adding %i to redirects dict...' % wid
        redirects[wid] = True

missing_titles = open('missing_titles.txt', 'w')
missing_redirects = open('missing_redirects.txt', 'w')

for doc in qi:
    wid = int(doc['id'])
    print 'Checking %i...' % wid
    if not titles.get(wid, False):
        print '%i is missing title data!' % wid
        missing_titles.write('%i\n' % wid)
    if not redirects.get(wid, False):
        print '%i is missing redirect data!' % wid
        missing_redirects.write('%i\n' % wid)

missing_titles.close()
missing_redirects.close()
