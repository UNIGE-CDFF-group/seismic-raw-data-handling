# seismic-raw-data-handling
Scripts for handling raw seismic data and convert to different formats.

How to convert datacube to MiniSEED
--------------------
The script `cube2mseed_jackseis.sh` is based on the `jackseis` tool
from [Pyrocko](https://pyrocko.org/)
The simplest way to run these scripts is using conda.
It is recommended to install the required libraries and packages 
inside a Conda environment to preserve your root environment. 
You can download Conda at the following [link](https://docs.conda.io/en/latest/miniconda.html).

Once you have installed conda, open a terminal (Linux) 
create a new environment with the following dependencies using:
```bash
conda config --add channels conda-forge
conda create -n pyrocko 
conda activate pyrocko
conda install -c pyrocko pyrocko
```

To convert the raw waveform data
**datacube** format to **miniSEED** for station PIAN:
```bash
cd seismic-raw-data-handling
# IMPORTANT: Before running the command below open the 
# cube2mseed_jackseis.sh file and change the path for the output
# to match your working directory (line 16)
bash cube2mseed_jackseis.sh
```
This should create a folder called `convertedTP/TP/PIAN` that includes
the converted miniSEED files. 

### TODO
___
- [ ] Automatize the process for converting datacube to MSEED



Last updated: *March 2023*