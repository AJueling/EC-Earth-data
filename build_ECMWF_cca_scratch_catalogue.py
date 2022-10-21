import os
import csv
from tqdm.autonotebook import tqdm

csv_file = open("ecmwf_cca_scratch.csv", "w")
writer = csv.writer(csv_file)
writer.writerow(['mip_era','activity_id','institution_id','source_id','experiment_id','member_id','table_id','variable_id','grid_label','version','dcpp_start_year','time_range','nc_path'])

for store in ['s2hh', 'xh2t']:  # 46 & 12 secs, respectively
    rootDir = f'/scratch/ms/nl/nm6/cmorised-results/EC-EARTH3P-HR-HighResMIP-highres-future/{store}/CMIP6/HighResMIP/'
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
