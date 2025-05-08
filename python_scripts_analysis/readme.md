# Analysis scripts in python

- extract_log.py: Python program that extracts Energy, PotEnergy, Temperature and pressure from a NAMD log file.
usage: simply type python extract_log.py name_of_your_log_file.log

- fitting_temp.py and fitting_temp_from_ETp_file.py: Program with calculation of T histogram and comparison with Theory. 
It analyses an input file with time series of T generated from NAMD log file (a T.dat 2 column file time vs T generated with VMD or a ETp file generated from the previous python program in this same repo). 
Comparison with theory requires to know number of degrees of freedom (see .log file)

- count_CO2.py: Example of MDAnalysis program counting the number of CO2 molecules inside a cavity. It is a good example of a case showing how to count the number of molecules or atoms verifying a given condition.

- water_inside_CNT.py: Counts number of water molecules inside a CNT. Another example of counting things.
- flow_water gives the number of molecules that crossed a given region (for example water molecules that crossed a membrane) as a function of frame or as a function of time.
- Calculate_applied_force.py: Calculates the applied force and pressure difference for NAMD nonequilibrium simulations with an external TCL force


A summary about analysis in MD Simulations can be found [here](https://saco.csic.es/s/yaZBGnDpaPERYsp)

Some scripts use MDAnalysis to analyze the trajectories (see [here](https://userguide.mdanalysis.org/stable/examples/quickstart.html) for a tutorial on How to Use MD Analysis)

