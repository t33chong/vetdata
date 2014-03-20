import requests
import sys
from bs4 import BeautifulSoup
from multiprocessing import Pool
from urllib2 import urlopen


def get_title_and_headline(wid):
    response = requests.get(
        'http://search-s10:8983/solr/main/select',
        params={'q': 'wid:%s AND is_main_page:true' % wid,
                'fl': 'url,wikititle_en', 'wt': 'json'}).json()

    try:
        doc = response.get('response', {}).get('docs', [{}])[0]

        url = doc.get('url', False)
        headline = doc.get('wikititle_en', '')

        title = ''
        if url:
            html = urlopen(url).read()
            soup = BeautifulSoup(html)
            title = soup.title.string.encode('utf-8')

        print '%s\t%s\t%s' % (wid, title, headline)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        print '%s\tERROR\tERROR' % wid

print 'wid\ttitle\theadline'
Pool(processes=8).map(
    get_title_and_headline,
    [line.strip() for line in open('topwams.txt').readlines()[:600]])
