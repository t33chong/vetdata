import os, shutil

xml_dir = '/data/xml'

for wid in os.listdir(xml_dir):
    if int(wid) == 831:
        continue
    wid_dir = os.path.join(xml_dir, wid)
    for pageid in os.listdir(wid_dir):
        first_digit = pageid[0]
        first_digit_dir = os.path.join(wid_dir, first_digit)
        if not os.path.exists(first_digit_dir):
            os.makedirs(first_digit_dir)
        pageid_file = os.path.join(wid_dir, pageid)
        shutil.move(pageid_file, first_digit_dir)
