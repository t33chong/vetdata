import sys

input_file = sys.argv[1]

events_dir = '/data/events/'

for wid in open(input_file):
    wid = wid.strip()
    print 'writing', wid
    query = 'wid:%s AND touched:[2013-09-30T23:59:59.999Z TO *] AND iscontent:true' % wid
    event_file = events_dir + wid
    with open(event_file, 'w') as f:
        f.write(query)
