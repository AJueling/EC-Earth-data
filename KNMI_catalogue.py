"""
This scripts creates an intake-esm catalogue of the EC-Earth3P data available at Philippe Le Sager's KNMI workstation
"""


import os
import csv

def attrs_from_namelist(name_list):
    """ parsing ECE3 output data attributes from the (non-CMIP-compliant) folder structure """
    assert len(name_list)==7

    if name_list[0] in ['Amon', 'Omon', 'SImon']:
        # ['Omon', 'control-1950', 'r3i1p2f1', 'hfds-control-lr', 'hfds', 'gn', 'v20190215']
        [table_id, experiment_id, member_id, _, variable_id, grid_label, version] = name_list
    elif name_list[0] in ['HiRes', 'LowRes']:
        # ['LowRes', 'Amon', 'control-1950', 'r1i1p2f1', 'rlut-control-lr', 'gr', 'v20190906']
        [_, table_id, experiment_id, member_id, variable_id, grid_label, version] = name_list
        if variable_id[-9:]=='-fullpath':       variable_id = variable_id[:-9]
        elif variable_id[-11:]=='-control-lr':  variable_id = variable_id[:-11]
        else: raise ValueError('unknown variable_id name')
    elif name_list[0]=='stream2-from-jasmin':
        # ['stream2-from-jasmin', 'LowRes', 'Omon', 'control-1950', 'r2i1p2f1', 'tos-control-lr', 'v20190815']
        [_, _, table_id, experiment_id, member_id, variable_id, version] = name_list
        variable_id = variable_id[:3]
    elif name_list[0]=='PRIMAVERA':
        # ['PRIMAVERA', 'stream2-from-jasmin', 'LowRes', 'Omon', 'control-1950', 'r2i1p2f1', 'soga']
        [_, _, _, table_id, experiment_id, member_id, variable_id] = name_list
        version = 'N/A'
    #elif name_list[0]=='users':
    #    # ['users', 'sager', 'PRIMAVERA', 'stream2-from-jasmin', 'LowRes', 'Amon', 'spinup-1900']
    #    [_,_,_,_,_,table_id, experiment_id] = name_list
    #    member_id = 'r1i1p2f1'
    #    variable_id = 
    #    grid_label = 'gr'
    #    version = 'N/A'
    else:
        raise ValueError(f'unknown folder structure: {name_list}')

    if name_list[0] in ['PRIMAVERA', 'stream2-from-jasmin']:
        if table_id=='Amon':    grid_label = 'gr'
        elif table_id=='Omon':  grid_label = 'gn'
        else: raise ValueError('need to supply grid_label')
            
    return experiment_id, member_id, table_id, variable_id, grid_label, version


if __name__ == "__main__":  # takes about a second to run
    csv_file = open("knmi_nc_ece3.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(['mip_era', 'activity_id', 'institution_id', 'source_id', 'experiment_id', 'member_id', 'table_id', 'variable_id', 'grid_label', 'version', 'dcpp_start_year', 'time_range', 'nc_path'])

    mip_era, activity_id = 'CMIP6', 'HighResMIP'
    institution_id = 'EC-Earth-Consortium'
    for i, store in enumerate(['HiRes', 'LowRes']):
        source_id = ['EC-Earth3P-HR','EC-Earth3P'][i]
        rootDir = f'/net/pc170547/nobackup_2/users/sager/PRIMAVERA/stream2-from-jasmin/{store}'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if not any(fname.endswith('.nc') for fname in fileList):  continue

            mip_era = 'CMIP6'
            name_list = os.path.normpath(dirName).split(os.path.sep)[-7:]
            if name_list[0]=='users':
                # ['users', 'sager', 'PRIMAVERA', 'stream2-from-jasmin', 'LowRes', 'Amon', 'spinup-1900']
                continue  # ignore spinup data
            experiment_id, member_id, table_id, variable_id, grid_label, version = attrs_from_namelist(name_list)
            nc_path = dirName+'/*.nc'
            writer.writerow([mip_era, activity_id, institution_id, source_id, experiment_id, member_id, table_id, variable_id, grid_label, version, '', '', nc_path])

    csv_file.close()