localfolder=`pwd`
$localfolder/getsite.py `cat site.txt`

ret=`${localfolder}/htmldiff.py`

echo $ret

if [ $ret == 0 ]

then
	echo unvariant
else
	echo changed
	notify-send changed
	date >> $localfolder/win.list 
fi
