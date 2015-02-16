#!/usr/bin/python2

import os

fscanf = open('lista.txt')

#leggo la lista dei file e genero una stringa per ogni nome
lista = fscanf.read()
listaS = str.splitlines(lista)
fscanf.close()
os.remove('lista.txt')

fscanf = open('lista.txt','a')
fscanf.write(listaS[1]+"\n")
fscanf.close()

ret = os.system("diff "+listaS[0]+" "+listaS[1])
os.remove(listaS[0])

print ret
