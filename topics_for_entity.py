import json
#from collections import defaultdict
#
#with open('entity_counts_for_topic_5000.json') as f:
#    entity_counts_for_topic = json.loads(f.read())
#
#topics_for_entity = defaultdict(list)
#
#for topic in entity_counts_for_topic:
#    for entity in entity_counts_for_topic[topic]:
#        topics_for_entity[entity].append(topic)
#
#with open('topics_for_entity.json', 'w') as g:
#    g.write(json.dumps(topics_for_entity))

with open('topics_for_entity.json') as i:
    topics_for_entity = json.loads(i.read())

with open('topics_for_entity.csv', 'w') as h:
    for entity in topics_for_entity:
        try:
            h.write(','.join([entity] + topics_for_entity[entity]).encode('utf-8') + '\n')
        except:
            print 'error'

with open('topic_count_for_entity.csv', 'w') as h:
    for entity in topics_for_entity:
        try:
            h.write('%s,%d\n'.encode('utf-8') % (entity, len(topics_for_entity[entity])))
        except:
            print 'error'
