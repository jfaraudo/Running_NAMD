# Analysis scripts in python

extract_log.py:
Python program that extracts Energy, PotEnergy, Temperature and pressure from a NAMD log file. 

fitting_temp.py: 
Program with calculation of T histogram and comparison with Theory. 
It analyses an input file T.dat with two columns (step or time) and T(K) (it can be easily created with VMD reading the .log file). 
Comparison with theory requires to know number of degrees of freedom (see .log file)

count_CO2.py:
Example of MDAnalysis program counting the number of CO2 molecules inside a cavity. It is a good example of a case showing how to count the number of molecules or atoms verifying a given condition.
