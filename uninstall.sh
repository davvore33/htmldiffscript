#!/bin/bash

echo this script will uninstall the routine and remove all files

read

localfolder=`pwd`

$localfolder/reinitialize.py

sudo rm /etc/cron.hourly/run.sh

rm -rf $localfolder
