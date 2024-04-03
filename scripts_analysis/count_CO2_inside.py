import MDAnalysis as mda
import pandas as pd
from matplotlib import pyplot as plt

dcd_files = ['../s1_NVT.dcd','../s2_NVT.dcd','../s3_NVT.dcd','../s4_NVT.dcd'] #Afegir els dcd que faci falta
C_data = []
time_data = []

def fun_C(): #Funció llista i grafica la quantitat de C al interior del MOP en funcio del temps
    
    C = []
    time = []
    f = open('CO2inside.dat','w')
    
    for ts in u.trajectory:
        C_w_int = u.select_atoms('type CG2O7 and sphzone 8.2 (resname BDC)')
        time.append(u.trajectory.time)
        C.append(len(C_w_int))
        f.write(f'{u.trajectory.time} {len(C_w_int)}\n')
    C_data.append(C)
    time_data.append(time)
    
    for i, C in enumerate(C_data):
        C_df = pd.DataFrame(C, columns = ['Number of carbons'], index=time)
        C_df.index.name = 'Time'

    C_df.plot(title='Number of C inside the MOP')
    plt.xlabel('Time')
    plt.ylabel('Number of C')
    plt.show()

for dcd_file in dcd_files:
    u = mda.Universe('../../build/new_final_CO2_solvate.psf', dcd_files) #change solvate.psf for the system's name

fun_C()

