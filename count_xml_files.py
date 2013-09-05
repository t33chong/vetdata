import os

xml_dir = '/data/xml'
count_dir = '/data/count'
if not os.path.exists(count_dir):
    os.makedirs(count_dir)

for wid in os.listdir(xml_dir):
    wid_dir = os.path.join(xml_dir, wid)
    count = 0
    for subdir in os.listdir(wid_dir):
        subdir = os.path.join(wid_dir, subdir)
        count += len(os.listdir(subdir))
    count_filename = os.path.join(count_dir, wid)
    with open(count_filename, 'w') as count_file:
        count_file.write(str(count))
