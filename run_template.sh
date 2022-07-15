#!/usr/bin/env bash
#SBATCH --account=s3673
#SBATCH --mem=50G
#SBATCH --time=12:00:00
#SBATCH --job-name=create_zarrs
#SBATCH --constraint="sky|hasw"
#SBATCH --output=outfiles/job_%j.out
#SBATCH --error=outfiles/job_%j.err

set -e

# Loading the required module
module load vim/8.1.2233
module load nano/2.6.3
module load python/GEOSpyD/Min4.10.3_py3.9
module load gdal/3.0.4
module load wget/1.20.3
echo "Using Python: $(which python)"

echo "*** Start time: $(date) *** "
# Run the script with time profiler
python3 -m cProfile -o zarr_time_profile make_zarr.py
echo "Zarrs completed"
echo "*** End time: $(date) *** "