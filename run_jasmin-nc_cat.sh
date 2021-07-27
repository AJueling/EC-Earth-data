#!/bin/bash
#SBATCH --partition=short-serial
#SBATCH --job-name=build_jasmin-nc_catalogue
#SBATCH --time=20:00:00
#SBATCH -o build_intake_cat_jasmin-nc_%A.out

source activate ECE
python build_intake_cat_jasmin-nc.py  >> build_intake_cat_jasmin-nc.out