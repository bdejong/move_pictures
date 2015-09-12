#! /usr/bin/env python

import exifread # pip install ExifRead
import datetime
import glob
import os
import argparse

parser = argparse.ArgumentParser(description='Move images')

parser.add_argument('--dryrun', action="store_true", default=False)
parser.add_argument('--inputpath', dest="inputpath", default=os.getcwd())
parser.add_argument('--outputpath', dest="outputpath", default=os.getcwd())

options = parser.parse_args()

print options

for filename in glob.glob(os.path.join(options.inputpath, "DSC_*.JPG")):
    tags = exifread.process_file(open(filename, 'rb'))

    picture_time = datetime.datetime.strptime(
        str(tags['Image DateTime']),
        '%Y:%m:%d %H:%M:%S')

    # move all pictures taken before 5 o'clock into the previous day
    picture_time = picture_time - datetime.timedelta(hours=5)

    directory_name = os.path.join(
        options.outputpath,
        "Nikon",
        picture_time.strftime("%Y-%m-%d__"))

    new_path = os.path.join(directory_name, os.path.basename(filename))

    if not os.path.exists(directory_name) and not options.dryrun:
        os.makedirs(directory_name)

    if not options.dryrun:
        os.rename(filename, new_path)

    print filename, "->", new_path
