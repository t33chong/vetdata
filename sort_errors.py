"""
Write error lines from dump_titles log to individual files.
"""

import re
from collections import defaultdict

failed = []

for line in open('dump_titles.errors'):
    match = re.search('([A-Z]+) SERVICE FAILED ON ([0-9]+)!', line)
    #print match.group(1), match.group(2)
    failed.append(match.group(2))

failed = list(set(failed))

with open('all.errors', 'w') as f:
    f.write('\n'.join(failed))
