import os
import csv

# rootDir = '/gws/nopw/j04/primavera2/stream1/PRIMAVERA/HighResMIP/'#EC-Earth-Consortium/EC-Earth3P-HR/' # 76 variables
# rootDir = '/gws/nopw/j04/primavera2/stream1/CMIP6/HighResMIP/'#EC-Earth-Consortium/EC-Earth3P-HR/' # 353 variables

csv_file = open("jasmin_nc_highresmip.csv", "w")
writer = csv.writer(csv_file)
writer.writerow(['mip_era','activity_id','institution_id','source_id','experiment_id','member_id','table_id','variable_id','grid_label','version','dcpp_start_year','time_range','nc_path'])

for store in ['CMIP6', 'PRIMAVERA']:
    rootDir = f'/gws/nopw/j04/primavera2/stream1/{store}/HighResMIP/'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if not any(fname.endswith('.nc') for fname in fileList):  continue
        os.path.normpath(dirName).split(os.path.sep)

        mip_era = 'CMIP6'
        name_list = os.path.normpath(dirName).split(os.path.sep)[-9:]
        [activity_id, institution_id, source_id, experiment_id, member_id, table_id, variable_id, grid_label, version] = name_list
        nc_path = dirName+'/*.nc'

        writer.writerow(['CMIP6']+name_list+2*['']+[dirName+'/*.nc'])

csv_file.close()