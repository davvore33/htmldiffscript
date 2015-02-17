#!/usr/bin/python2

import os
localfolder = os.getcwd()
readinglist = open(localfolder+'/list.txt')

#I'm writing the list and I'll push every name in a string matrix
list = readinglist.read()
listS = str.splitlines(list)
readinglist.close()
os.remove(localfolder+'/list.txt')

writinglist = open(localfolder+'/list.txt','a')
writinglist.write(listS[1]+"\n")
writinglist.close()

ret = os.system("diff "+listS[0]+" "+listS[1])
os.remove(listS[0])

print ret
