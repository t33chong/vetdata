import os
import sys
import json
import gzip
from multiprocessing import Pool
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from WikiaSolr import QueryIterator
from nlp_client import title_confirmation
from nlp_client.services import AllTitlesService

title_confirmation.USE_S3 = False

docs = [wid.strip() for wid in open('missing-titles.txt')]

titles_dir = '/data/titles/'

bucket = S3Connection().get_bucket('nlp-data')
k = Key(bucket)

def call_titles(doc):
    try:
        print 'Calling AllTitlesService on', doc
        titles = json.dumps(AllTitlesService().get(doc), ensure_ascii=False)
        titles_file = titles_dir + doc + '.gz'
        g = gzip.GzipFile(titles_file, 'w')
        g.write(titles)
        g.close()
        k.key = 'article_titles/%s' % os.path.basename(titles_file)
        k.set_contents_from_filename(titles_file)
        os.remove(titles_file)
    except:
        print doc, 'failed!'
        raise

pool = Pool(processes=7)
pool.map(call_titles, docs)
