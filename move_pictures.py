#! /usr/bin/env python

import exifread # pip install ExifRead
import datetime
import glob
import os


for filename in glob.glob("*.JPG"):
    tags = exifread.process_file(open(filename, 'rb'))
    
    picture_time = datetime.datetime.strptime(str(tags['Image DateTime']), '%Y:%m:%d %H:%M:%S')
    
    picture_time = picture_time - datetime.timedelta(hours=5) # move all pictures taken before 5 o'clock into the previous day
    
    directory_name = picture_time.strftime("%Y-%m-%d__")
    
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        
    os.rename(filename, os.path.join(directory_name, filename))
    
    print filename, "->", directory_name
