#!/usr/bin/python2

import sys
import urllib
import datetime
import os

localfolder=os.getcwd()

url=sys.argv[1]
date=str(datetime.datetime.now().time()) #python datatime lib return "now" time, composed by hour, min, sec and decimal, maybe ever files will be different nomined
filename=localfolder+"/index"+date+".html"

print("url= "+url)
print("istant "+date)

fprintf = open(localfolder+'/list.txt','a')
fprintf.write(filename+"\n")
urllib.urlretrieve(url, filename=filename) #finally catching the html file, nomined "filename"

fprintf.close()
