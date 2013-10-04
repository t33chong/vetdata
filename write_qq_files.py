events_dir = '/data/events/'

for wid in open('wids.txt'):
    wid = wid.strip()
    print 'writing', wid
    query = 'wid:%s AND iscontent:true' % wid
    event_file = events_dir + wid
    with open(event_file, 'w') as f:
        f.write(query)
