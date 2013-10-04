from WikiaSolr import QueryIterator

qi = QueryIterator('http://search-s10:8983/solr/xwiki/', {'query': 'lang_s:en', 'fields': 'id', 'sort': 'wam_i desc', 'start': 0, 'limit': 1000})

f = open('top1k', 'w')

for doc in qi:
    f.write('%s\n' % doc['id'])

f.close()
