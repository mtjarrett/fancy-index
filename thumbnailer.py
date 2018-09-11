#/usr/bin/python
import os
#check and/or create hidden thumbnail directory
if os.path.isdir("/var/www/html/sites/images/.thumbnails") == False:
  os.system("mkdir /var/www/html/sites/images/.thumbnails")
#cycle through file and add thumbnails to thumbnail directory
for filename in os.listdir("/var/www/html/sites/images"):
  if filename.endswith(".jpg"):
    os.system("convert -thumbnail 256x256 /var/www/html/sites/images/%s /var/www/html/sites/images/.thumbnails/thumb.%s" % (filename,filename))
    continue
  else:
    continue
