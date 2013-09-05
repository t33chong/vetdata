"""
Print the expected and actual counts of parsed content articles per wiki.
"""

import os, subprocess, requests

print "=id=\t=url=".ljust(40)+"\t==expected==\t==actual=="
for wid in os.listdir('/data/xml'):
    xmlCount = sum([len(os.listdir('/data/xml/%s/%s' % (wid, subdir))) for subdir in os.listdir('/data/xml/'+wid)])
    doc = requests.get('http://search-s10:8983/solr/xwiki/select', params={'wt':'json', 'q':'id:%s'%wid, 'fl':'id,url,articles_i'}).json().get('response', {}).get('docs', [{}])[0]
    print "%s\t%s\t%s\t%s" % (str(doc.get('id')), doc.get('url').ljust(40), str(doc.get('articles_i')).ljust(10), str(xmlCount).ljust(10))

        
