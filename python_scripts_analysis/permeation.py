# This script identifies water molecules that permeate through the
# nanotube layer

import MDAnalysis as mda
import numpy as np

# --- region of crossing ---
upper_end = 6.754
lower_end = -6.754

# Start counting permeation events after this number of frames
skip_frame = 0
output_file = "permeation.dat"

# Load your trajectory (replace with your own files)
u = mda.Universe('../input/system.psf','MD.dcd')
wat = u.select_atoms("name OH2")

seg_list = wat.segids  # Per-atom segid
resids = wat.resids    # Per-atom resid
num_atoms = len(wat)
labels = np.zeros(num_atoms, dtype=int)

num1 = 0  # +z direction count
num2 = 0  # -z direction count

# Each water molecule has a label, which has 5 possible values
#  2: Above the nanotube layer
# -2: Below the nanotube layer
#  1: Inside the nanotube layer, entering from upper surface
# -1: Inside the nanotube layer, entering from lower surface
#  0: Inside the nanotube layer from the beginning

# For every frame, the label of each water molecule is
# determined, and compared with its label in the previous frame.
# If the new label is +2 (or -2), while the old label is -1 (or +1),
# it means the water molecule has traversed the nanotube, thus a
# permeation event is reported and counted. If a water molecule
# is inside the nanotube layer in the current frame, its label
# will be determined by its old label.

print("Computing permeation events... (please wait)")

with open(output_file, "w") as f:
    f.write("# frame +z -z \n")

    for ts in u.trajectory:
        z_coords = wat.positions[:, 2]
        old_labels = labels.copy()
        for i, z in enumerate(z_coords):
            old_label = old_labels[i]
            segname = seg_list[i]
            resid = resids[i]

            if z > upper_end:
                new_label = 2
                if old_label == -1:
                    print(f"{segname}:{resid} permeated through the nanotubes along +z direction at frame {ts.frame}")
                    if ts.frame >= skip_frame:
                        num1 += 1
            elif z < lower_end:
                new_label = -2
                if old_label == 1:
                    print(f"{segname}:{resid} permeated through the nanotubes along -z direction at frame {ts.frame}")
                    if ts.frame >= skip_frame:
                        num2 += 1
            elif abs(old_label) > 1:
                new_label = old_label // 2
            else:
                new_label = old_label

            labels[i] = new_label

        # Save data to file
        f.write(f"{round(ts.time)} {num1} {num2}\n")

# Summary
nf = len(u.trajectory) - skip_frame
if nf >= 0:
    print(f"\nThe total number of permeation events during {nf} frames in +z direction is: {num1}")
    print(f"The total number of permeation events during {nf} frames in -z direction is: {num2}")
else:
    print(f"The specified first frame ({skip_frame}) is larger than the total number of frames.")

print("Time evolution saved in a .dat file")
