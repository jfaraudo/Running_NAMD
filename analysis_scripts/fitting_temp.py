#
# Program calculation of T histogram and comparison with Theory
# 
# By Jordi Faraudo
# Based on a program by Alberto Gil
#
# Input data: two column file with step number and T in K
#
import numpy
from numpy import sqrt, pi, exp, linspace, loadtxt, power
import matplotlib.pyplot as plt 
#import pylab as pl
#from matplotlib.ticker import MaxNLocator
#from scipy.optimize import curve_fit

# ---------------------------------------------------------------------------
# Function Instantaneous Temperature distribution at equilibrium 
# (Gaussian)
#
def tempboltz(T,Ttermo,sigma):
	return (1./(sqrt(2.*pi)*sigma))*exp(-(T-Ttermo)*(T-Ttermo)/(2.*sigma*sigma))
# -----------------------------------------------------------------------------
#
# Main Program
#


print('Anaylisis of T from MD simulations')
print('----------------------------------')

#Ask for number of degrees of freedom
Nu = int(input("\n Number of Degrees of freedom:\n>"))

#Read file with temperature from simulation data
temps = loadtxt('T.dat')
temps = temps[:,1] 

#Compute Average temperature
tavg = numpy.average(temps) 
print('\nThermodynamic Temperature estimated from data file:',tavg,' K\n')

sigma=sqrt(2.*tavg*tavg/Nu)
print('\nSigma due to finite size of system:',sigma,' K\n')

#Create figure
plt.figure(dpi=150)

tmin=tavg-4.0*sigma
tmax=tavg+4.0*sigma
#Generate a plot with the theoretical function 
T=numpy.arange(tmin,tmax,0.005)
plt.plot(T,tempboltz(T,tavg,sigma),'-k',lw=2,label='Theoretical\n Distribution')

#Calculate a normalised histogram of the temperatures from the data 
plt.hist(temps,density=1, bins=100)

#Define axis
plt.axis([tmin, tmax, 0, 0.08]) #axis([xmin,xmax,ymin,ymax])

plt.xlabel("Instantaneous T (K)",size=12)
plt.ylabel("Probability",size=12)

#Show the plot
plt.show()


