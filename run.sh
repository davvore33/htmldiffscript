./getsite.py `cat site.txt`

ret=`./htmldiff.py`

echo $ret

if [ $ret == 0 ]

then
	echo unvariant
else
	echo changed
	notify-send changed
	date >> win.list 
fi
