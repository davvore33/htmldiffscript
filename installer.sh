localefolder=`pwd`
sudo ln -s $localfolder/run.sh /etc/cron.hourly/run.sh

echo I\'ve linked run.sh in /etc/cron.hourly

echo Now i need the site that you wanna check

read site

echo $site > $localfolder/site.txt

echo $site is the entry, now I\'m gonna initialize the routine

$localfolder/getsite.py `cat site.txt`
