from WikiaSolr import QueryIterator

qi = QueryIterator('http://dev-search:8983/solr/xwiki/', {'query': 'lang_s:en', 'fields': 'id', 'sort': 'wam_i desc', 'limit': 1500})

with open('/data/top1500.txt', 'w') as f:
    for doc in qi:
        f.write(doc['id'] + '\n')
