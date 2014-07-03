import requests
import sys
import traceback
from multiprocessing import Pool
from nlp_services.document_access import ListDocIdsService
from pprint import pprint

wid = sys.argv[1]
step = 50
#step = 10


def chunks(array, n):
    """Yield successive n-sized chunks from array"""
    for i in xrange(0, len(array), n):
        yield array[i:i+n]


def get_fields(doc_ids):
    print 'Getting fields for %s' % doc_ids
    array = []
    r = requests.get(
        '%swikia.php' % url,
        params={'controller': 'WikiaSearchIndexer',
                'method': 'get',
                'service': 'All',
                #'ids': doc_ids_subset}
                'ids': '|'.join(doc_ids)}
        )
    try:
        indexer = r.json().get('contents', [])
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        print traceback.format_exc()
        indexer = []
    #pprint(indexer)
    if indexer:
        for doc in indexer:
            if doc.get('id') is not None:
                array.append(
                    (doc['id'],
                     (doc.get('headings_mv_%s' % lang, {}).get('set', []) +
                      doc.get('categories_mv_%s' % lang, {}).get('set', []))))
                #indexed[doc['id']] = (
                #    doc.get('headings_mv_%s' % lang, {}).get('set', []) +
                #    doc.get('categories_mv_%s' % lang, {}).get('set', []))
    return array

#foo = range(100)
#print map(lambda x:x, chunks(foo, 9))
#sys.exit(0)

details = requests.get(
    'http://www.wikia.com/api/v1/Wikis/Details/',
    params={'ids': wid}).json().get('items', {}).get(wid)
#doc_ids_combined = {}
#indexed = {}
if details is not None:
    url = details.get('url')
    lang = details.get('lang')
    #print url
    #doc_ids = ListDocIdsService().get_value(wid)
    doc_ids = map(lambda x: x.split('_')[1],
                  filter(lambda y: '_' in y,
                         #ListDocIdsService().get_value(wid)))[:100]
                         ListDocIdsService().get_value(wid)))
    #pprint(doc_ids); sys.exit(0)
    #for n in range(0, len(doc_ids), step):
    ##for n in range(0, 20, step):
    #    print 'n = %d' % n
    #    doc_ids_subset = doc_ids[n:n+step]
    r = Pool(processes=8).map_async(get_fields, chunks(doc_ids, step))
    r.wait()
    pprint(r.get())
    print '*'*80
    #for k in r.get():  # DEBUG
    #    print k
    fields = []
    m = map(lambda x: fields.extend(x), r.get())
    #pprint(fields)
    indexed = dict(fields)

pprint(indexed)  # DEBUG

#for doc_id in doc_ids_to_heads:
#    entity_response = doc_ids_to_entities.get(
#        doc_id, {'titles': [], 'redirects': {}})
#    doc_ids_combined[doc_id] = map(preprocess,
#                                   indexed.get(doc_id, []) +
#                                   entity_response['titles'] +
#                                   entity_response['redirects'].keys() +
#                                   entity_response['redirects'].values() +
#                                   list(set(doc_ids_to_heads.get(doc_id,
#                                                                 []))))
