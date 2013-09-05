"""
Gzip all XML files and delete the originals.
"""

import os, shutil, gzip

xml_dir = '/data/xml'

for wid in os.listdir(xml_dir):
    wid_dir = os.path.join(xml_dir, wid)
    for subdir in os.listdir(wid_dir):
        subdir_path = os.path.join(wid_dir, subdir)
        for xml_file in os.listdir(subdir_path):
            xml_path = os.path.join(subdir_path, xml_file)
            gzip_filepath = xml_path + '.gz'
            gzip_file = gzip.GzipFile(gzip_filepath, 'w')
            gzip_file.write(open(xml_path).read())
            gzip_file.close()
            os.remove(xml_path)
