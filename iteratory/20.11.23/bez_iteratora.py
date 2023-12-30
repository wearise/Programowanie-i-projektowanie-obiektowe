from protein_structure import *

strctr = read_pdb_content("2GB1", open("2gb1.pdb"))
all_atoms = []
for chain in strctr.chains():
    for residue in chain.residues():
        # all_atoms.append(residue.atoms())
        for atom in residue.atoms():
            all_atoms.append(atom.name)
            print(atom.name)
print(all_atoms)