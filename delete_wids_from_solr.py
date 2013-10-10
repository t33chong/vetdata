"""
Update Solr - delete all queries for wiki IDs that no longer exist.
Input file is a newline-separated file of wiki IDs to delete.
"""

import json
import requests

for line in open('delete_from_solr.txt'):
    update = json.dumps({'delete': {'query': 'wid:%s' % line.strip()}})
    requests.post('http://search-s11.prod.wikia.net:8983/solr/update/json?commit=true', data=update, headers={'Content-type': 'application/json'})
