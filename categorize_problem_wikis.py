from collections import defaultdict

d = defaultdict(dict)

for line in open('title-urls-unix.txt'):
    wid, url, category = line.strip().split('\t')
    d[category][wid] = url

for category in d:
    with open('wiki-category-%s.txt' % category, 'w') as f:
        f.write('\n'.join(['%s\t%s' % (wid, d[category][wid]) for wid in d[category]]))
