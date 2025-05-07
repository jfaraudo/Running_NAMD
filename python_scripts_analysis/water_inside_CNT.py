#Import MDAnalysis
import MDAnalysis as mda
import matplotlib.pyplot as plt

#Load trajectory
simulacio = mda.Universe('imdnanotube.psf','autoimd.dcd')

#init list
time =[]
waterin=[]

#Loop over frames calculating water inside as a funciton of time
for ts in simulacio.trajectory:
    time.append(simulacio.trajectory.time)
    waterin.append(len(simulacio.select_atoms('type OT and prop abs z <6.7')))

#Plot
plt.plot(time,waterin)
plt.xlabel('Time (ps)')
plt.ylabel('Number molecules inside')
plt.title('Simulation of Water Molecules inside a Nanotube')
plt.show()
