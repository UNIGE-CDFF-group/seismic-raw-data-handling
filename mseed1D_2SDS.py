#!/usr/bin/env python
"""
Script to convert MSEED data to SEISCOMP DATA STRUCTURE by Channel
The code is meant to work with 1 day or near 1 day duration data
Requirements: Obspy 
Usage: mseed1D_SDS.py input_file.mseed

N Perez nperez@sgc.gov.co
F munoz fjmunozb@unal.edu.co


"""
from obspy.core import UTCDateTime
from obspy.core import read
import numpy as np
from glob import glob
import sys
import os
import shutil

if len(sys.argv)<2:
        print("Check your input")
        sys.exit()

for file in sys.argv[1:]:
    st = read(file)
    st.merge(method=1, fill_value='interpolate')
    if len(st)>3:
        stZ = st.select(channel='*Z')
        stZ.merge()
        print(stZ)
        stE = st.select(channel='*E')
        stE.merge()
        print(stE)
        stN = st.select(channel='*N')
        stN.merge()
        print(stN)
        st1 = stZ+stE+stN
        print(st1)
        for tr in st1:
            if isinstance(tr.data, np.ma.masked_array):
                tr.data = tr.data.filled()
    else:
        st1 = st.copy()


    for tr in st1:
        tr.stats.network = 'DP' #change the name of your network
        tr.stats.location = '00' #change or keep emty the location code of your station
        #tr.decimate(factor=5, no_filter=True, strict_length=False) #uncomment if you need to resample the trace
        t = tr.stats.starttime
        if t.julday < 10:
            julday = '00'+str(t.julday) # to deal with julian days 
        elif 10 <= t.julday < 100:
            julday = '0'+str(t.julday)
        else:
            julday = str(t.julday)
        tr_name = tr.stats.network+'.'+tr.stats.station+'.'+tr.stats.location+'.'+tr.stats.channel+'.'+'D'+'.'+str(t.year)+'.'+julday
        tr.write(tr_name, format='MSEED',encoding='STEIM2', reclen=512)
        
        #uncomment the following two lines and adapt the path where you want to store your output. Otherwhise the output will be stored in the local directory.
        #target  = r'DATA/2021/DP'+'/'+tr.stats.station+'/'+tr.stats.channel+'.D'  
        #shutil.move(tr_name,target)
        
        print(tr_name, '--->   written')
