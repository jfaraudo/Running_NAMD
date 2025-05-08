# This script counts the total net water flow through the
# nanutube layer in the trajectory

# Before running it, first load the dcd file in VMD, and make sure
# it's the "top" molecule.

# Specify the upper and lower boundaries of the nanotube layer
# data for practical J Faraudo
import MDAnalysis as mda
import numpy as np

# Settings
upper_end = 6.754
lower_end = -6.754
output_file = "flow.dat"

# Load trajectory (change filenames as needed)
u = mda.Universe('../input/system.psf','MD.dcd')
wat = u.select_atoms("name OH2")

# The following function sets the status for each water molecule
# status 0: Inside the nanotube layer
# status 1: Above the nanotube layer
# status -1: Below the nanotube layer
def get_status(z_coords):
    status = []
    for z in z_coords:
        if z < lower_end:
            status.append(-1)
        elif z > upper_end:
            status.append(1)
        else:
            status.append(0)
    return np.array(status)

# Initialization
u.trajectory[0]  # First frame
old_status = get_status(wat.positions[:, 2])
total = 0

# For every frame, the status of each water molecule is
# calculated, and compared with its status in the previous frame.
# If the status changes from 0 to +-1 or vice versa, it means that
# this water molecule has crossed one of the boundaries of the
# nanotube layer. The variable "total" records the total number
# of such crossing events (for each event, either +1 or -1 is
# added to "total", according to the crossing direction). However,
# due to the periodic boundary condition, a change of the status
# from +1 to -1 or vice versa doesn't mean the water molecule has
# crossed the channel.

with open(output_file, "w") as f:
    for ts in u.trajectory[1:]:
        new_status = get_status(wat.positions[:, 2])
        for old, new in zip(old_status, new_status):
            if old != new and old + new != 0:
                total += new - old
        old_status = new_status.copy()
        f.write(f"{round(ts.time)} {total/2.0}\n")

# The net flow is taken as the average of the numbers of the
# crossing events for the two boundaries, i.e., one half of "total"
# Final output
if total > 0:
    print(f"The net flow is {total / 2.0} water molecules along +z")
elif total < 0:
    print(f"The net flow is {-total / 2.0} water molecules along -z")
else:
    print("The net flow is 0")
print("Time evolution saved in a .dat file")
