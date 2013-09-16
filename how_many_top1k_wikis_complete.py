import os

complete = []
complete_dir = '/data/complete_xml'
for filename in os.listdir(complete_dir):
    for line in open(os.path.join(complete_dir, filename)):
        complete.append(line.strip())
complete = set(complete)

top1k = set([line.strip() for line in open('/data/top1500.txt')])

complete_top1k = complete & top1k

print '%i top1k wikis parsed' % len(complete_top1k)
