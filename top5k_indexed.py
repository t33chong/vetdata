import requests

SOLR = 'http://search-s10:8983/solr/xwiki/select'
DATE = '2013-09-30T23:59:59.999'

params = {
             'q':'lang_s:en',
             'fl':'id',
             'facet': 'true',
             'facet.limit': '100', # -1
             'facet.query': 'indexed:[%sZ TO NOW]' % DATE,
             'facet.field': 'id',
             'wt': 'json'
         }


r = requests.get(SOLR, params=params).json()

#from pprint import pprint; pprint(r)

# TODO: convert facet_fields list to dict, test wids in top5k.txt against them for True or False, return back keys for which value is True
ids = r['facet_counts']['facet_fields']['id']
d = dict((ids[i], ids[i+1]) for i in range(0, len(ids), 2))
print d

#for line in open('top5k.txt'):
#    wid = line.strip()

wids = filter(lambda x: d.get(x), [l.strip() for l in open('top5k.txt')])

print wids
