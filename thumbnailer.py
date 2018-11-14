#!/usr/bin/python
import os
import sys
import re

rootDir = "/var/www/html/image/"
#rootDir = sys.argv[1]

#Recursive walkthrough from "rootDir"
for dirName, subdirList, fileList in os.walk(rootDir):
	#print ("Checking for changes in directory: \'%s\'" % (dirName))

	#ignore hidden folders (starting with ".")
	subdirList[:] = [d for d in subdirList if not d[0] == '.'] 

	#check and/or create hidden thumbnail directory
		
	if (os.path.isdir("%s/.thumbnails/" % (dirName)) == False):
		os.system("mkdir \'%s\'/.thumbnails" % (dirName))

	#cycle through file and add thumbnails to thumbnail directory
	for filename in os.listdir('%s' % (dirName)):

		#image thumbnailer
		if (filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".svg") or filename.endswith(".jpeg") or filename.endswith(".JPG")  or filename.endswith(".gif") or filename.endswith(".tiff") or filename.endswith(".tif") or filename.endswith(".bmp")):
			fileTime = float(os.path.getctime("%s/%s" % (dirName, filename)))			
			stripFile = os.path.splitext(os.path.basename(filename))[0]
			filename = filename.replace('*','\*')
			stripFile2 = stripFile.replace('*','\*')
			
			if(os.path.isfile("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile))):
				thumbTime = float(os.path.getctime("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile)))
			else:
				thumbTime = 0.0
			if ((fileTime) > thumbTime):
				#print("Thumbnailing: \'%s\'/\'%s\'" % (dirName, filename))
				os.system("convert -thumbnail 256x256 \'%s\'/\'%s\' \'%s\'/.thumbnails/thumb.\'%s\'.jpg" % (dirName, filename, dirName, stripFile2))
				if '\*' in stripFile2:
					os.system("mv \"%s/.thumbnails/thumb.%s.jpg\" \"%s/.thumbnails/thumb.%s.jpg\"" % (dirName, stripFile2, dirName, stripFile))



		#pdf thumbnailer      
		elif (filename.endswith(".pdf")):
			stripFile = os.path.splitext(os.path.basename(filename))[0]
			filename = filename.replace('*','\*')
			stripFile2 = stripFile.replace('*','\*')

			if(os.path.isfile("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile))):
				thumbTime = float(os.path.getctime("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile)))
			else:
				thumbTime = 0.0
			if ((fileTime) > thumbTime):
				os.system("convert -colorspace sRGB \'%s\'/\'%s\'[0] -scale 256x256 -background white -flatten \'%s\'/.thumbnails/thumb.\'%s\'.jpg" % (dirName, filename, dirName, stripFile2))
			if '\*' in stripFile2:
				os.system("mv \"%s/.thumbnails/thumb.%s.jpg\" \"%s/.thumbnails/thumb.%s.jpg\"" % (dirName, stripFile2, dirName, stripFile))
				
				
		#video thumbnailer      
		elif (filename.endswith(".mp4")):
			stripFile = os.path.splitext(os.path.basename(filename))[0]
			filename = filename.replace('*','\*')
			stripFile2 = stripFile.replace('*','\*')

			if(os.path.isfile("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile))):
				thumbTime = float(os.path.getctime("%s/.thumbnails/thumb.%s.jpg" % (dirName, stripFile)))
			else:
				thumbTime = 0.0
			if ((fileTime) > thumbTime):
				os.system("convert \'%s\'/\'%s\'[100]  \'%s\'/.thumbnails/thumb.\'%s\'.png" % (dirName, filename, dirName, stripFile2))
			if '\*' in stripFile2:
				os.system("mv \"%s/.thumbnails/thumb.%s.jpg\" \"%s/.thumbnails/thumb.%s.jpg\"" % (dirName, stripFile2, dirName, stripFile))

			

			
			