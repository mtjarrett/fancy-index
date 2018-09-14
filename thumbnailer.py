#!/usr/bin/python
import os
import sys

#rootDir = "/var/www/html/images"
rootDir = sys.argv[1]
print("%s" % rootDir)

for dirName, subdirList, fileList in os.walk(rootDir):
  subdirList[:] = [d for d in subdirList if not d[0] == '.'] 

  #check and/or create hidden thumbnail directory
  if os.path.isdir("%s/.thumbnails" % (dirName)) == False:
    os.system("mkdir %s/.thumbnails" % (dirName))
    
    
  #cycle through file and add thumbnails to thumbnail directory
  
  for filename in os.listdir("%s" % (dirName)):
    
    #add image file extensions
    if (filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".svg") or filename.endswith(".jpeg")  or filename.endswith(".gif") or filename.endswith(".tiff") or filename.endswith(".bmp")):
      fileTime = float(os.path.getctime("%s/%s" % (dirName, filename)))
      if(os.path.isfile("%s/.thumbnails/thumb.%s" % (dirName, filename))):
        thumbTime = float(os.path.getctime("%s/.thumbnails/thumb.%s" % (dirName, filename)))
      else:
        thumbTime = 0.0
      if (fileTime > thumbTime):
          os.system("convert -thumbnail 256x256 %s/%s %s/.thumbnails/thumb.%s" % (dirName, filename, dirName, filename))
          continue
          
    #pdf thumbnailer      
    elif (filename.endswith(".pdf")):
      fileTime = float(os.path.getctime("%s/%s" % (dirName, filename)))
      if(os.path.isfile("%s/.thumbnails/thumb.%s.bmp" % (dirName, filename))):
        thumbTime = float(os.path.getctime("%s/.thumbnails/thumb.%s.bmp" % (dirName, filename)))
      else:
        thumbTime = 0.0
      if (fileTime > thumbTime):
        os.system("convert -thumbnail 256x256 %s/%s %s/.thumbnails/thumb.%s.bmp" % (dirName, filename, dirName, filename))
        continue
            
    else:
      continue
