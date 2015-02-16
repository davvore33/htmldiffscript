#!/usr/bin/python2

import sys
import urllib
import datetime
import os

print("script per controllare i cambiamenti di una pagina, passare come primo parametro la url della pagina da controllare nella forma \"http://url\"")

url=sys.argv[1]
date=str(datetime.datetime.now().time())
filename="index"+date+".html"

print("url= "+url)
print("momento "+date)

fprintf = open('lista.txt','a')
fprintf.write(filename+"\n")
urllib.urlretrieve(url, filename=filename)

fprintf.close()
