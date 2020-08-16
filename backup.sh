#!/bin/bash

#set -x

# What to backup? 
backup_files="Test.{htm,json,py}"

# Backup to

#dest="/backupfolder"

# Create archive filename
archive_file="/backupfolder/bck_`date +%Y%m%d`.tar"


tar -cf /backupfolder/bck_`date +%Y%m%d`.tar Test.{htm,json,py}

if [ `echo $?` -ne 0 ]
then
    echo "Backup Failed!"
else
    echo "Backup Success!"
fi
