import exifread # pip install ExifRead
import datetime
import glob
import os

for filename in glob.glob("*.JPG"):
    tags = exifread.process_file(open(filename, 'rb'))
    
    picture_time = str(tags['Image DateTime'])
    
    picture_time = datetime.datetime.strptime(picture_time, '%Y:%m:%d %H:%M:%S')
    
    picture_time = picture_time - datetime.timedelta(hours=5) # move all pictures taken before 5 o'clock into the previous day
    
    directory = picture_time.strftime("%Y-%m-%d__")
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    os.rename(filename, os.path.join(directory, filename))
    
    print filename, picture_time