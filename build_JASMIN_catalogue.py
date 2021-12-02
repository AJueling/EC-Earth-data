import os
import csv

# rootDir = '/gws/nopw/j04/primavera2/stream1/PRIMAVERA/HighResMIP/'#EC-Earth-Consortium/EC-Earth3P-HR/' # 76 variables
# rootDir = '/gws/nopw/j04/primavera2/stream1/CMIP6/HighResMIP/'#EC-Earth-Consortium/EC-Earth3P-HR/' # 353 variables

csv_file = open("jasmin_nc_highresmip.csv", "w")
writer = csv.writer(csv_file)
writer.writerow(['mip_era','activity_id','institution_id','source_id','experiment_id','member_id','table_id','variable_id','grid_label','version','dcpp_start_year','time_range','nc_path'])

for store in ['CMIP6', 'PRIMAVERA']:
    print(store)
#     rootDir = f'/gws/nopw/j04/primavera2/stream1/{store}/HighResMIP/'
    rootDir = f'/badc/cmip6/data/{store}/HighResMIP/EC-Earth-Consortium/'
    for dirName, subdirList, fileList in os.walk(rootDir, followlinks=True):
        if os.path.normpath(dirName).split(os.path.sep)[-1]!='latest':  continue
        if os.path.normpath(dirName).split(os.path.sep)[-4][-3:]!='mon':  continue
        if not any(fname.endswith('.nc') for fname in fileList):  continue
        print(dirName)
        os.path.normpath(dirName).split(os.path.sep)

        mip_era = 'CMIP6'
        name_list = os.path.normpath(dirName).split(os.path.sep)[-9:]
#         print(name_list)
        [activity_id, institution_id, source_id, experiment_id, member_id, table_id, variable_id, grid_label, version] = name_list
        if activity_id!='HighResMIP':  continue
        if institution_id!='EC-Earth-Consortium':  continue
        if grid_label not in ['gn','gr']:  continue
        nc_path = dirName+'/*.nc'

        writer.writerow(['CMIP6']+name_list+2*['']+[dirName+'/*.nc'])

csv_file.close()