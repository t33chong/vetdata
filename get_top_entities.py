# Write top entities for top N wam wikis to CSV
from multiprocessing import Pool
from nlp_client.caching import useCaching
from nlp_client.services import TopEntitiesService

useCaching(dontCompute=True)

def get_entities(wid):
    return wid, [entity for (entity, count) in TopEntitiesService().nestedGet(wid)]

wids = [line.strip() for line in open('topwams.txt').readlines()[:5000]]
with open('top_entities.csv', 'w') as f:
    for (wid, entities) in Pool(processes=8).map(get_entities, wids):
        print(','.join([wid] + entities).encode('utf-8') + '\n')
        f.write(','.join([wid] + entities).encode('utf-8') + '\n')
