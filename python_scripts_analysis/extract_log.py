#
# Python code to extract Energy, Temperature and Pressure from NAMD log file
#

# write the name of the log file when executing the script. For example:
# python extract_log.py NVT.log

import sys,os
import numpy as np

# Assign to "a_" the name of log file provided with input
a_ = sys.argv[1]

#It has to be a .log file
if a_.split('.')[-1] != 'log':
   raise TypeError('Hardcoded to work for NAMD style log files with a .log extension')

# Check whether we have an output file from a previous run
if os.path.isfile(a_.split('.log')[0] + '_output.dat'):
   raise ValueError('Output file still exists :: delete that and retry')

#Create TWO output files
g_ = open(a_.split('.log')[0] + '_output.dat','a') #generic unformatted output
file2= open(a_.split('.log')[0] + '_ETp.dat', 'w') #formatted TS, energy, Temp, p output
fileheader="# step Etot Epot T p \n"
file2.write(f'{fileheader}')

#Init counter
count_T = 0

#Read data from LOG file and save relevant data to generic unformatted output
with open(a_,'r') as f_:
    for line in f_:
        if line[0:6] == "ETITLE":
           count_T += 1
           if count_T == 1:
              g_.write(line)
        if line[0:6] == "ENERGY":
              g_.write(line)
g_.close()

#read the data from generic unformatted output
d= np.genfromtxt(a_.split('.log')[0] + '_output.dat',skip_header=1,usecols=[1,11,12,13,16])

#Format the data and save in a formatted output file
num_steps=d[:,0].size  #number of time steps in the simulation

for i in range(num_steps):
   d_step = d[i,:]
   file2.write(f'{int(d_step[0])} {d_step[1]} {d_step[3]} {d_step[2]} {d_step[4]} \n') #save TS, Etotal, Epotential, Temp and pressure


