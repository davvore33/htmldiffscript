localfolder=`pwd`

if [ $1 == ""]
then
	$localfolder/getsite.py `cat site.txt`
else
	$localfolder/getsite.py $1
fi

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
