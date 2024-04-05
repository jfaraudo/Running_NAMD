# Analysis scripts in python

extract_log.py:
Python program that extracts Energy, PotEnergy, Temperature and pressure from a NAMD log file. 

fitting_temp.py and fitting_temp_from_ETp_file.py: 
Program with calculation of T histogram and comparison with Theory. 
It analyses an input file with time series of T generated from NAMD log file (a T.dat 2 column file time vs T generated with VMD or a ETp file generated from the previous python program in this same repo). 
Comparison with theory requires to know number of degrees of freedom (see .log file)

count_CO2.py:
Example of MDAnalysis program counting the number of CO2 molecules inside a cavity. It is a good example of a case showing how to count the number of molecules or atoms verifying a given condition.
