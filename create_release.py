#!/usr/bin/env python
import os
import zipfile

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

if __name__ == '__main__':
    plugins = ['service.zfs']
    for plugin in plugins:
        zipf = zipfile.ZipFile('./releases/%s/service.zfs-0.0.2.zip'%plugin, 'w')
        zipdir('./%s'%plugin, zipf)
        zipf.close()
