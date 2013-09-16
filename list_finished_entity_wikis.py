"""
Given the console output of entity-overseer.py, write a newline-separated list of
wikis for which entity extraction has already been completed.
"""

import re

finished = []
for line in open('entity-done.txt'):
    done = re.match('Finished wid ([0-9]+) in [0-9]+ seconds with return status 0', line)
    if done:
        finished.append(done.group(1))

print finished
print len(finished)

with open('entity-skip.txt', 'w') as skip:
    skip.write('\n'.join(finished))
