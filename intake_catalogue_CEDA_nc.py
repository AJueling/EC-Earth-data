import os
import csv
from tqdm.autonotebook import tqdm

csv_file = open("ceda_nc_highresmip.csv", "w")
writer = csv.writer(csv_file)
writer.writerow(['mip_era','activity_id','institution_id','source_id','experiment_id','member_id','table_id','variable_id','grid_label','version','dcpp_start_year','time_range','nc_path'])

for store in ['CMIP6', 'PRIMAVERA']:  # 46 & 12 secs, respectively
    rootDir = f'/badc/cmip6/data/{store}/HighResMIP/'
    print(store)
    print(os.listdir(rootDir))
    for dirName, subdirList, fileList in tqdm(os.walk(rootDir)):
        if not any(fname.endswith('.nc') for fname in fileList):  continue
        os.path.normpath(dirName).split(os.path.sep)

        mip_era = 'CMIP6'
        name_list = os.path.normpath(dirName).split(os.path.sep)[-9:]
        [activity_id, institution_id, source_id, experiment_id, member_id, table_id, variable_id, grid_label, version] = name_list
        nc_path = dirName+'/*.nc'

        writer.writerow(['CMIP6']+name_list+2*['']+[dirName+'/*.nc'])

csv_file.close()