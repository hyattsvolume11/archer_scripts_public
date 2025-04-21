# -- Copy_to_S3Bucket.EXAMPLE.MobaXterm.ps1 --
# for test runs in mobaXterm - shell utility on windows jump box
#
# python imports (from 2022)
import awscliv2 
import subprocess
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# use aws s3 cp to copy tenable ip info to archer s3 bucket
#
# local file information
# file: c://my_archer_scripts_location/the_generated_daily_archer_copy.csv
# locally copy file to: c://my_archer_scripts_location/BACKUPS/ - with date
# s3 bucket : s3://MY_ARCHER_DATA_S3_BUCKET/
# s3 bucket location for data copy: s3://MY_ARCHER_DATA_S3_BUCKET/MY_ARCHER_VULN_DATA/

# get date 
date = datetime.now().strftime("%m%d%Y")
# windows file paths
myfile = 'C:/my_archer_scripts_location/the_generated_daily_archer_copy.csv'

#make new local file with date in backup directory
newfile = 'C:/my_archer_scripts_location/BACKUPS/the_generated_daily_archer_copy.csv' + date

# copy file date to local backup directory file
from shutil import copyfile
copyfile(myfile, newfile)

# use aws s3 cp to copy tenable ip info to archer s3 bucket

# copy archer data to s3 
push=subprocess.call(['aws', 's3', 'cp', 'c://my_archer_scripts_location/the_generated_daily_archer_copy.csv', 's3://MY_ARCHER_DATA_S3_BUCKET/MY_ARCHER_VULN_DATA/', '--profile=default'])
#print(push.returncode)

