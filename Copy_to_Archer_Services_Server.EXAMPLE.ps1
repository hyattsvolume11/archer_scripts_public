#
# copy-item using powershell -- copy csv to local Windows server location 

Copy-Item c://my_archer_scripts_location/the_generated_daily_archer_copy.csv \\TESTING_ARCHER_STAGING_SERVER\Archer_Data_feeds\Nessus_Data\
Copy-Item c://my_archer_scripts_location/the_generated_daily_archer_copy.csv \\TESTING_ARCHER_loc\Archer_Data_feeds\Nessus_Data\
