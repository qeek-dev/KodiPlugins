#!/usr/bin/env python
import os
import zipfile

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('./releases/service.zfs_0.0.1.zip', 'w')
    zipdir('./service.zfs', zipf)
    zipf.close()
