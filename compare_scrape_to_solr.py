import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen


def get_title_and_headline(wid):
    response = requests.get(
        'http://search-s10:8983/solr/main/select',
        params={'q': 'wid:%s AND is_main_page:true' % wid,
                'fl': 'url,headline_txt', 'wt': 'json'}).json()

    doc = response.get('response', {}).get('docs', [{}])[0]

    url = doc.get('url', False)
    headline = doc.get('headline_txt', '')

    title = ''
    if url:
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        title = soup.title.string.encode('utf-8')

    print '%s,%s,%s' % (wid, title, headline)

print 'wid,title,headline'
for line in open('topwams.txt').readlines()[:500]:
    get_title_and_headline(line.strip())
