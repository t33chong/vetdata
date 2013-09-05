"""
Delete text files that have already been parsed.
Pass currently parsing wids as arguments at command line, e.g.:
python count_xml_files.py 123 456 789
"""
import os, sys, shutil

to_delete = [int(wid) for wid in sys.argv[1:]]

text_dir = '/data/text'

for wid in os.listdir(text_dir):
    if int(wid) in to_delete:
        continue
    wid_dir = os.path.join(text_dir, wid)
    shutil.rmtree(wid_dir)
