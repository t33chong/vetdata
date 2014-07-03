#import requests
#from boto.s3.connection import S3Connection
#from boto.s3.key import Key
#
#SOLR = 'http://search-s10:8983/solr/main/select'
#bucket = S3Connection().get_bucket('nlp-data')

# ORIGINAL
#with open('parsed_stats.txt', 'w') as f:
#    print 'wid\ttotal\tparsed'
#    print >>f, 'wid\ttotal\tparsed'
#    for line in open('top5k.txt'):
#        wid = line.strip()
#        r = requests.get(SOLR, params={'q': 'wid:%s AND iscontent:true' % wid, 'fl': 'id', 'wt': 'json'}).json()
#        count = r['response']['numFound']
#        parsed = len(filter(lambda x: x.key.endswith('.xml'), bucket.list('xml/%s/' % wid)))
#
#        s = '%s\t%s\t%d' % (wid, count, parsed)
#        print s
#        print >> f, s

#redo = []
for line in open('parsed_stats.txt').readlines()[1:]:
    wid, total, parsed = line.strip().split('\t')
    total = float(total)
    parsed = float(parsed)
    if total > 0:
        ratio = parsed / total
    else:
        ratio = 0.0
    if ratio <= 0.8:
        print wid
        #redo.append(wid)

#print len(redo)
