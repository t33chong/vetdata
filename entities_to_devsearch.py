import json
import requests

SOLR_URL = 'http://dev-search:8983/solr/xwiki/update?commit=true'

docs = []

for line in open('top_entities.csv'):
    line = line.strip()
    split = line.split(',')
    wid = split[0]
    doc = dict(id=wid)
    print wid
    entities = split[1:]
    doc['entities_txt'] = {'set': entities}
    docs += [doc]

print requests.post(SOLR_URL, data=json.dumps(docs), headers={'Content-type': 'application/json'}).content
