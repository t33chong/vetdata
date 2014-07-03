from __future__ import division
import requests
import traceback

#solr = 'http://search-s10:8983/solr/xwiki/select'
solr = 'http://search-s10:8983/solr/main/select'

for line in open('mysqlquery.txt'):
    try:
        wid, count = map(int, line.strip().split())
        #r = requests.get(solr, params={'q': 'id:%d' % wid, 'fl': 'pages_i', 'wt': 'json'})
        r = requests.get(solr, params={'q': 'wid:%d AND iscontent:true' % wid, 'fl': 'wid', 'wt': 'json'})
        #solr_count = int(r.json()['response']['docs'][0]['pages_i'])
        solr_count = int(r.json()['response']['numFound'])

        if solr_count == 0:
            ratio = 0
        else:
            ratio = count/solr_count
        if ratio < 0.8:
            print wid
    except:
        pass
