import MDAnalysis as mda

#List of dcd files
dcd_files = ['../push_water_1/MD.dcd']

#load simulaiton files
simulacio = mda.Universe('../input/system.psf',dcd_files)

#select 
seleccioW = simulacio.select_atoms("type OT and prop z <= 20 and prop z >= 10", updating=True)

#Value of Applied force in NAMD units
forceNAMD = 1.0
#convert to pN
force = 69.493 *forceNAMD
#Surface membrane (A**2)
AM = 23.0*19.919

#Output file
fitxer= open('Applied_Force.dat', 'w') 
fitxer.write("# time(ps) Nwater Force (pN) Pressure Dif (atm) \n")

#Loop: calculate
for ts in simulacio.trajectory:
    temps_actual = round(ts.time)
    frame_actual = ts.frame
    numW = seleccioW.n_atoms

    #total force in pN
    forcetot = force*numW
    #pressure in atm
    presdif = (forcetot/AM)*(1000.0/1.013)
    
    #print data
    print(f"Frame: {frame_actual:4d},Time {temps_actual:4.0f} ps, N= {numW:4.0f}, F= {forcetot:4.0f} pN, dp= {presdif:4.0f} atm")
    #save data
    fitxer.write(f'{temps_actual} {numW} {forcetot} {presdif}\n') #save number of monomers

