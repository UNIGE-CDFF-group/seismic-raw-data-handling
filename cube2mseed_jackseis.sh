#!/bin/bash

#Script to convert from datacube to mseed and change the header
#requisites: pyrocko

station=temporary #directory name wich contains your data cube inputs
for st in $station
	do

	echo $station
	cd $station
	
	
	echo 'converting files to mseed ...'


        jackseis *.A* --tinc=86400 --rename-channel='/p0/HHZ/' --rename-channel='/p1/HHN/' --rename-channel='/p2/HHE/' \
		--rename-network='/.*/DP/' \
		--output='./convertedTEMP/%n/%s/%n.%s..%c.D.%(wmax_year)s.%j' #set up your output path. If not, the output will go to the directory "temporary" 

	cd ..

done
