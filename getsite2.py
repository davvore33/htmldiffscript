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

#writinglist = open(localfolder+'/list.txt','a')
#writinglist.write(filename+"\n")
retrived=urllib.urlopen(url).info()
retrived=str.splitlines(str(retrived))

print retrived	#TODO: devo capire se posso richiedere solo Date/Last-modified dato che google.it e kernel.org rispondono in due modi diversi con nomenclature diverse [viva gli standard]


#writinglist.close()
