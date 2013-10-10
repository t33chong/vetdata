import sys
import json
import requests

widsfile = sys.argv[1]

for wid in open(widsfile):
    try:
        docs = json.loads(requests.get('http://search-s11.prod.wikia.net:8983/solr/main/select', params={'q': 'wid:%s' % wid, 'fl': 'url', 'wt': 'json'}).content)['response']['docs']
        url = docs[0]['url']
    except IndexError:
        url = 'NONE'
    print wid.strip() + '\t' + url
