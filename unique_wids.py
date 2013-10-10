titles = set([wid.strip() for wid in open('dump-titles.log.wids')])
redirects = set([wid.strip() for wid in open('dump-redirects.log.wids')])

print 'titles - redirects'
titles_less_redirects = list(titles - redirects)
print '\n'.join(titles_less_redirects)

print 'redirects - titles'
redirects_less_titles = list(redirects - titles)
print '\n'.join(redirects_less_titles)
