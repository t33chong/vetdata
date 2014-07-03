from __future__ import division
import numpy
from math import sqrt
from pipeline.event import QueryIterator

q = QueryIterator(
    'http://search-s10:8983/solr/xwiki/',
    {'query': 'lang_s:en', 'fields': 'id,pages_i', 'sort': 'wam_i desc',
     'limit': 100})
     #'limit': 5000})

#for doc in q:
#    print doc['id'], doc['pages_i']

#pagecounts = [int(doc['pages_i']) for doc in q][:2500]
#pagecounts = sorted([int(doc['pages_i']) for doc in q])[:4500]

id_to_count = [(int(doc['id']), int(doc['pages_i'])) for doc in q][:20]
for wid, pages in id_to_count:
    print '%s\t%s' % (wid, pages)
import sys; sys.exit(0)

#id_to_count = sorted([(int(doc['id']), int(doc['pages_i'])) for doc in q],
#                     key=lambda x: x[1])[:90]

pagecounts = map(lambda x: x[1], id_to_count)
#print pagecounts

#mean = sum(pagecounts)/len(pagecounts)
#print 'mean:', mean
#std = sqrt(sum(map(lambda x: (x - mean)**2, pagecounts))/len(pagecounts))
#print 'std:', std

arr = numpy.array(pagecounts)
mean = numpy.mean(arr)
std = numpy.std(arr)

#id_to_count = [(int(doc['id']), int(doc['pages_i'])) for doc in q]
#pagecounts = sorted(pagecounts, key=lambda x: x[1])
#

for wid, pages in id_to_count:
    print wid, pages

print 'len:', len(pagecounts)
print 'mean:', mean
print 'std:', std
