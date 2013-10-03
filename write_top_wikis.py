from WikiaSolr import QueryIterator

events_dir = '/data/events/'

qi = QueryIterator('http://search-s10:8983/solr/xwiki/', {'query': 'lang_s:en', 'fields': 'id', 'sort': 'wam_i desc', 'start': 1000})

for doc in qi:
    print 'writing', doc['id']
    query = 'wid:%s AND iscontent:true' % doc['id']
    event_file = events_dir + doc['id']
    with open(event_file, 'w') as f:
        f.write(query)
