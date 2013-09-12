import os

with open('/data/this_xmldirs.txt', 'w') as f:
    f.write('\n'.join(os.listdir('/data/xml')))
