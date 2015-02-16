#!/usr/bin/python2

import sys
import urllib
import datetime
import os

url=sys.argv[1]
date=str(datetime.datetime.now().time()) #python datatime lib return "now" time, composed by hour, min, sec and decimal, maybe ever files will be different nomined
filename="index"+date+".html"

print("url= "+url)
print("istant "+date)

fprintf = open('list.txt','a')
fprintf.write(filename+"\n")
urllib.urlretrieve(url, filename=filename) #finally catching the html file, nomined "filename"

fprintf.close()
