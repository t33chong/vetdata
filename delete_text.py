import os, shutil

text_dir = '/data/text'

for wid in os.listdir(text_dir):
    if int(wid) == 31618 or int(wid) == 283 or int(wid) == 912 or int(wid) == 124137:
        continue
    wid_dir = os.path.join(text_dir, wid)
    shutil.rmtree(wid_dir)
