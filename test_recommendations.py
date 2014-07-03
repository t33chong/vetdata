import requests
import sys

csv = sys.argv[1]

d = {}
for line in open(csv):
    if ',' in line:
        parts = line.strip().split(',')
        d[parts[0]] = parts[1:]

while True:
    pageid = raw_input('\nEnter a page id: ')
    related = d.get(pageid, [])
    for article in related:
        r = requests.get(
            'http://search-s11:8983/solr/main/select',
            params={'q': 'id:%s' % article, 'fl': 'title_en', 'wt': 'json'})
        #print r.json()['response']['docs'][0]['title_en']
        docs = r.json().get('response', {}).get('docs')
        if docs:
            print docs[0].get('title_en', '')
