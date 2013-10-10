import re
import sys

logfile = sys.argv[1]

wids = [re.match('FAILED! ([0-9]+)', line).group(1) for line in open(logfile)]

with open(logfile + '.wids', 'w') as f:
    f.write('\n'.join(wids))
