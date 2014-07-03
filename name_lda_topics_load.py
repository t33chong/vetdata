from __future__ import division

# Attempt to make sense of topic features by identifying the top entities
# common to them across different wikis, calculating Jaccard distance against
# top entities per wiki, and naming the topic feature after the best-fit wiki

import json
import logging
import requests
import sys
import traceback
from collections import defaultdict
from identify_wiki_subjects import identify_subject
from multiprocessing import Pool
from nlp_client.caching import useCaching
from nlp_client.services import TopEntitiesService
from wiki_recommender import as_euclidean, get_topics_sorted_keys

# Specify how many of the top wikis to iterate over
top_n = int(sys.argv[1])

SOLR_URL = 'http://dev-search:8983/solr/xwiki/select'

useCaching(dontCompute=True)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
fh = logging.FileHandler('name_lda_topics_load.log')
fh.setLevel(logging.ERROR)
log.addHandler(fh)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
log.addHandler(sh)

# Jaccard functions taken from https://github.com/mouradmourafiq/data-analysis
def jaccard_sim(tup_1, tup_2, verbose=False):
    """Calculate the Jaccard similiarity of 2 tuples"""
    sum = len(tup_1) + len(tup_2)
    set_1 = set(tup_1)
    set_2 = set(tup_2)
    inter = 0
    for i in (set_1 & set_2):
        count_1 = tup_1.count(i)
        count_2 = tup_2.count(i)
        inter += count_1 if count_1 < count_2 else count_2
    j_sim = inter/sum
    if verbose : print j_sim
    return j_sim

def jaccard_distance(tup_1, tup_2):
    """Calculate the Jaccard distance between 2 tuples"""
    return 1 - jaccard_sim(tup_1, tup_2)

def name_topic(topic):
    """Given a topic, return the best-fit title based on Jaccard distance from
    a wiki's top entities"""
    log.info('Finding title for ' + topic)
    # Make sure topic is in dictionary
    if not entity_counts_for_topic.get(topic, False):
        return (topic, '')
    # Get top 50 entities associated with topic
    s = sorted(entity_counts_for_topic[topic].items(), key=lambda x: x[1],
               reverse=True)
    topic_entities = [k for (k, v) in s[:50]]
    # Find all wikis containing topic entities
    wids = []
    for topic_entity in topic_entities:
        wids.extend(wikis_for_entity.get(topic_entity, []))
    wids = list(set(wids))
    # Compute Jaccard distance 
    distances = [(wid, jaccard_distance(topic_entities, entities_for_wiki[wid]))
                 for wid in wids]
    best_wid, best_distance = min(distances, key=lambda x: x[1])
    log.debug('Jaccard distances: %s\nClosest: %s' % (distances, best_wid))
    title = identify_subject(best_wid, terms_only=True)
    return (topic, title)

log.info('Loading entity counts for topic')
with open('entity_counts_for_topic_%d.json' % top_n) as a:
    entity_counts_for_topic = json.loads(a.read())
log.info('Loading entities for wiki')
with open('entities_for_wiki_%d.json' % top_n) as b:
    entities_for_wiki = json.loads(b.read())
log.info('Loading wikis for entity')
with open('wikis_for_entity_%d.json' % top_n) as c:
    wikis_for_entity = json.loads(c.read())

#import pdb; pdb.set_trace()

# Write best-fit title per topic feature to CSV
with open('topic_names_%d_wikis.csv' % top_n, 'w') as f:
    for (topic, title) in Pool(processes=8).map(name_topic,
                                                entity_counts_for_topic.keys()):
        try:
            f.write('%s,%s\n'.encode('utf-8') % (topic, title))
        except:
            log.error('%s: %s' % (topic, traceback.format_exc()))

#with open('topic_names_%d_wikis.csv' % top_n, 'w') as f:
#    for topic in entity_counts_for_topic.keys():
#        f.write('%s,%s\n'.encode('utf-8') % name_topic(topic))
