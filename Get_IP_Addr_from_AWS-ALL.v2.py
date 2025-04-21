# -- Get_IP_Addr_from_AWS-ALL.v2.py -- 
#  Build CSV file from EC2 instance IP address data based on System Tag(Business Service) and Enviroment Tag(s)
#  to import into Fileserver or S3 bucket for processing

# python lib imports (from 2022)
import boto3
import time
import csv
from tenable.sc import TenableSC
#
# Version 2 - add output to a file instead of trying to redirect
# Created August 2022

# EC2 initialize 
ec2 = boto3.resource('ec2')

# open CSV file for writing 
csv_file = open("c:/my_archer_scripts_location/the_generated_daily_archer_copy.csv", "w")

# variables - from AWS Tags: 
# my_BS = System Tag in AWS => Business Service/Application/System Name
# my_Env = Environment Tag in AWS => Prod/Production | Stage/Staging | Dev/Development | Test/Testing

# write IP list found into CSV with Business Service and Environment 
# csv_file.write(str(my_list) + "," + my_BS + "," + my_Env + "\n")

# Example 1 
# BS = SharePoint_Example_01
# Env = Stage 
# Date Added 12/21/21
filters = [
    {'Name': 'tag:System', 'Values': ['SharePoint_Example_01']},
    {'Name': 'tag:Environment', 'Values': ['*tage']}
]
my_list = []
my_BS = "SharePoint_Example_01"

# Set to Stage - - ignore case issue
my_Env = "Stage"
for instance in ec2.instances.filter(Filters=filters):
    if instance.state["Name"] != "running":
        continue
    my_list = format(instance.private_ip_address)
    csv_file.write(str(my_list) + "," + my_BS + "," + my_Env + "\n")

# Example 2
# BS = SharePoint_Example_02
# Env =  Production
# Date Added - 08/08/1950
filters = [
    {'Name': 'tag:System', 'Values': ['SharePoint_Example_02']},
    {'Name': 'tag:Environment', 'Values': ['*roduction']}
]

my_list = []
my_BS = "SharePoint_Example_02"
# Set To "Production" - ignore case issue
my_Env = "Production"
for instance in ec2.instances.filter(Filters=filters):
    if instance.state["Name"] != "running":
        continue
    my_list = format(instance.private_ip_address)
    csv_file.write(str(my_list) + "," + my_BS + "," + my_Env + "\n")

# sleep for a minute after every 10 systems added 
#time.sleep(60) # Delay for 1 minute (60 seconds).

# Example 3 -
# All "Non Prod" systems : get Staging and Dev info with extra filtering 
# BS = MainWebSite
# ENV =  Stage & Dev
# Added 12/21/2021
filters = [
    {'Name': 'tag:System', 'Values': ['MainWebSite']},
    {'Name': 'tag:Environment', 'Values': ['*tage']}
]
# 2nd filter for additional Env
filters2 = [
    {'Name': 'tag:System', 'Values': ['MainWebSite']},
    {'Name': 'tag:Environment', 'Values': ['*evelop']}
]

my_list = []
my_BS = "MainWebSite"
# set to "Stage and Develop" for CSV 
my_Env = "Stage and Develop"
for instance in ec2.instances.filter(Filters=filters):
    if instance.state["Name"] != "running":
           continue
    my_list = format(instance.private_ip_address)
    csv_file.write(str(my_list) + "," + my_BS + "," + my_Env + "\n")
    

for instance in ec2.instances.filter(Filters=filters2):
    if instance.state["Name"] != "running":
        continue
    my_list = format(instance.private_ip_address)
    csv_file.write(str(my_list) + "," + my_BS + "," + my_Env + "\n")

# Example 4 - special tag/filter 
# extra tag: "IsInSpecialNetwork" -> True
# BS - MyExtraNetwork
# Env = Stage 
# Date Added - 08/08/1951
filters = [
    {'Name': 'tag:IsInSpecialNetwork', 'Values': ['*rue']},
    {'Name': 'tag:Environment', 'Values': ['*tage']}
]

my_list = []
my_BS = "MyExtraNetwork"
my_Env = "Stage"
# Set to "Stage" to ignore Case 
for instance in ec2.instances.filter(Filters=filters):
    if instance.state["Name"] != "running":
        continue
    my_list = format(instance.private_ip_address)
    csv_file.write(str(my_list) + "," + my_BS + "," + my_Env + "\n")

# sleep for a minute after every 10 systems 
#time.sleep(60) # Delay for 1 minute (60 seconds).


#after all systems added, close csv file
csv_file.close()

# EOF
