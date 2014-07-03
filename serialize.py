import json
import requests
from WikiaSolr import QueryIterator

SOLR = 'http://search-s10:8983/solr/xwiki/'

qi = QueryIterator(SOLR, {'query': 'lang_s:en', 'fields': 'id, hostname_s', 'sort': 'id asc'})

d = {}

for wiki in qi:
    try:
        print wiki['id'], wiki['hostname_s']
    except:
        print 'unicode error'
    d[int(wiki['id'])] = wiki['hostname_s']

with open('hostnames.json', 'w') as f:
    f.write(json.dumps(d))
