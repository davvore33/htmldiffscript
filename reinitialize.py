#!/usr/bin/python2

import os

localfolder=os.getcwd()

print "this script will reinitialize entire routine"

try:
	readinglist = open(localfolder+'/list.txt')
	list = readinglist.read()
	listS = str.splitlines(list)
	readinglist.close()
	os.remove(localfolder+'/list.txt')
	i=len(listS)
	while i > 0:
		try:
			os.remove(listS[i-1])
		except:
			print "there is no "+list[i-1]
		i=i-1
except:
	print "there is no list"

try:
	os.remove(localfolder+'/site.txt')
except:
	print "there is no site"
try:
	os.remove(localfolder+'/win.list')
except:
	print "there is no win"
