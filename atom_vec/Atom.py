from Vec3 import Vec3


class Atom(Vec3):

    def __init__(self, atom_no, name, *args):
        """Represents a chemical atom"""
        super(Atom, self).__init__(*args)
        self.__id = atom_no
        self.__name = name

    def to_pdb(self):
        return "ATOM   %4d %4s  ARG A   3    %8.3f%8.3f%8.3f  0.50 35.88           N" % \
            (self.__id, self.__name, self.x, self.y, self.z)

    @property
    def name(self):
        return self.__name

    @property
    def element(self):
        return self.__element


def atoms_from_pdb(pdb_fname):
    atoms = []
    for atom_line in open(pdb_fname):
        atom_number = int(atom_line[6:11].strip())
        x_position = float(atom_line[30:38].strip())
        y_position = float(atom_line[38:47].strip())
        z_position = float(atom_line[47:54].strip())
        atom_name = atom_line[12:16].strip()
        atoms.append(Atom(atom_number, atom_name, x_position, y_position, z_position))
    return atoms


class ChargedAtom(Atom):
    """represents an atom with a charge (might be fractional)"""

    def __init__(self, atom_no, name, q):
        super(ChargedAtom, self).__init__(atom_no, name)
        self.__q = q


if __name__ == "__main__":
    v = Vec3(1.3, 2.4, 3.4)
    a = Atom(1, " CA ")
    qa = ChargedAtom(1, " NZ ", 1.0)

    # ---------- Atoms behave like vectors: you can add them, or add a vector to an atom
    print(a.to_pdb())
    a += v
    print(a.to_pdb())

    v_cm = Atom(1, "C")
    atoms = atoms_from_pdb("surpass.pdb")
    for atom in atoms: v_cm += atom
    v_cm *= 1.0 / len(atoms)
    print("center of mass:", v_cm)