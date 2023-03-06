#!/bin/bash
# Bash script to convert data format from datacube to mseed and change the header
# requisites: pyrocko (see readme for installation instructions)
station_code=PIAN
path2rawdata='raw_data'
for st in $path2rawdata
	do
	echo $path2rawdata
	cd $path2rawdata
	cd $station_code

	echo 'converting files to mseed ...'
        jackseis * --tinc=86400 --rename-channel='/p0/HHZ/' --rename-channel='/p1/HHN/' --rename-channel='/p2/HHE/' \
		--rename-network='/.*/TP/' \
		--rename-station='/\d{3}/'$station_code/ \
		--output='/home/user_name/path2codes/seismic-raw-data-handling/convertedTEMP/%n/%s/%n.%s..%c.D.%(wmax_year)s.%j' #set up your output path. If not, the output will go to the directory "temporary"
	cd ..

done

