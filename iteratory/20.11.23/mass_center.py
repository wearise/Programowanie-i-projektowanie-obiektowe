from protein_structure import *

strctr = read_pdb_content("2GB1", open("2gb1.pdb"))
n, cm_x, cm_y, cm_z = 0, 0.0, 0.0, 0.0
for b in strctr.residues():
    for a in b.atoms():
        cm_x += a.x
        cm_y += a.y
        cm_z += a.z
        n += 1
cm_x /= n
cm_y /= n
cm_z /= n
