# EC-Earth-data
intake-esm catalogues of EC-Earth3(P)-(HR) and some HighResMIP data at JASMIN/CEDA, ECMWF, KNMI

The `MIPVariableNames.csv` files comes from

## 1. intake-esm catalogues

While these catalogues can be read with intake-esm, you need to have access to the servers in order to load any of the data.

### 1.1 CEDA CMIP6

The catalogue is `https://raw.githubusercontent.com/cedadev/cmip6-object-store/master/catalogs/ceda-zarr-cmip6.json`
This is unfortunately neither complete not up to date.

### 1.2 CEDA HighResMIP netCDF: `ceda_nc_highresmip.json`

from both CMIP6 and PRIMAVERA archives

### 1.3 JASMIN HighResMIP netCDF: `jasmin_nc_highresmip.json`

from both CMIP6 and PRIMAVERA archives 

A catalogue of file that are stored both in:

`/gws/nopw/j04/primavera2/stream1/PRIMAVERA/HighResMIP/` and `/gws/nopw/j04/primavera2/stream1/CMIP6/HighResMIP/`

The json file is created manually (from the `ceda-zarr-cmip6.json` above).
The csv is compiled with `os.walk` in `JASMIN_catalogue.py` (excuted from within jupyterlab with the activated `venv-cmip6-zarr` virtual environment). 

### 1.4 ECMWF


### 1.5 KNMI EC-Earth3(P)-(HR): `knmi_nc_ece3.json`

Some ECE3 data is stored at `/usr/people/sager/nb2/PRIMAVERA/stream2-from-jasmin/`


### 1.5 Google CMIP6

`https://storage.googleapis.com/cmip6/pangeo-cmip6.json`

---

## 2. data availability

