./htmldiffscript.py `cat sito.txt`

ciao=`./htmldiff.py`

echo $ciao

if [ $ciao == 0 ]

then
	echo sito invariato
else
	echo sito cambiato
	notify-send sito cambiato
	date >> win.list 
fi
