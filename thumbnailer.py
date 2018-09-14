#!/usr/bin/python
import os
import sys

#rootDir = "/var/www/html/images"
rootDir = sys.argv[1]

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
      stripFile = os.path.splitext(os.path.basename(filename))[0]
      if(os.path.isfile("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile))):
        thumbTime = float(os.path.getctime("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile)))
      else:
        thumbTime = 0.0
      if (fileTime > thumbTime):
          os.system("convert -thumbnail 256x256 %s/%s %s/.thumbnails/thumb.%s.jpg" % (dirName, filename, dirName, stripFile))
          continue
          
    #pdf thumbnailer      
    elif (filename.endswith(".pdf")):
      fileTime = float(os.path.getctime("%s/%s" % (dirName, filename)))
      stripFile = os.path.splitext(os.path.basename(filename))[0]
      if(os.path.isfile("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile))):
        thumbTime = float(os.path.getctime("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile)))
      else:
        thumbTime = 0.0
      if (fileTime > thumbTime):
        os.system("convert -colorspace sRGB %s/%s -scale 256x256 -background white -flatten %s/.thumbnails/thumb.%s.jpg" % (dirName, filename, dirName, stripFile))
        continue
            
    else:
      continue

      
      #print os.path.splitext(os.path.basename("hemanth.txt"))[0]