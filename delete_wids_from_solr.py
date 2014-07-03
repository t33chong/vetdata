"""
Update Solr - delete all queries for wiki IDs that no longer exist.
Input file is a newline-separated file of wiki IDs to delete.
"""

import sys
import json
import requests

to_delete = sys.argv[1]

for line in open(to_delete):
    update = json.dumps({'delete': {'query': 'wid:%s' % line.strip()}})
    requests.post('http://search-s11:8983/solr/update/json?commit=true', data=update, headers={'Content-type': 'application/json'})
