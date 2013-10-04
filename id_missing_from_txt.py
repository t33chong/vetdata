import re
from boto.s3.connection import S3Connection
from boto.s3.key import Key

bucket = S3Connection().get_bucket('nlp-data')

print 'loading titles...'
titles = dict((re.search('/([0-9]+)\.gz', title.key).group(1), True) for title in bucket.list(prefix='article_titles/') if re.search('/([0-9]+)\.gz', title.key))
print 'loading redirects...'
redirects = dict((re.search('/([0-9]+)\.gz', redirect.key).group(1), True) for redirect in bucket.list(prefix='article_redirects/') if re.search('/([0-9]+)\.gz', redirect.key))

t = open('missing-titles.txt', 'w')
r = open('missing-redirects.txt', 'w')

#for parsed in bucket.list(prefix='xml/', delimiter='/'): # source is xml s3 bucket
for parsed in open('top1k'): # source is text file containing top n
    #print parsed.name
    #s = re.search('([0-9]+)', parsed.name) # source is xml s3 bucket
    s = re.search('([0-9]+)', parsed) # source is text file containing top n
    if s:
        print 'checking', s
        wid = s.group(0)
        if not titles.get(wid, False):
            print wid, 'not found in titles!'
            t.write('%s\n' % wid)
        if not redirects.get(wid, False):
            print wid, 'not found in redirects!'
            r.write('%s\n' % wid)

t.close()
r.close()
