from __future__ import annotations

import itertools
import math
from dataclasses import dataclass, field
from typing import Dict


class AtomsInChainIterator:  # powinno pamiętać current residue i
    def __init__(self, chain: Chain):
        self.__residues = list(chain.residues())
        self.__current_residue = 0
        self.__current_atom = 0

    def __next__(self):
        try:  # sprawdź, czy możesz dać (__curent_atom+1) atom z __curent_residue
            self.__current_atom += 1
            return self.__residues[self.__current_residue].atoms()[self.__current_atom - 1]
        except:
            self.__current_residue += 1
            self.__current_atom = 1

            try:
                return self.__residues[self.__current_residue].atoms()[self.__current_atom - 1]
            except:
                raise StopIteration

        # jak zwróci wyjątek to pniemy się w górę, aż będzie na końcu StopIteration
        # dlatego najpierw się przesuwa, a potem zwraca i-1 element, bo po returnie nie jesteśmy już w stanie nic zmieić
        # pilnujemy, jak chcemy pozostawić po returnie

        # __next__ - przesuwa o 1 i zwraca aktualny

class ResiduesInStructureIterator:  # powinno pamiętać current residue i
    def __init__(self, strct: Structure):
        self.__chains = list(strct.chains())
        self.__current_chain = 0
        self.__current_residue = 0

    def __next__(self):
        try:  # sprawdź, czy możesz dać (__curent_atom+1) atom z __curent_residue
            self.__current_residue += 1
            return list(self.__chains[self.__current_chain].residues())[self.__current_residue - 1]
        except:
            self.__current_residue += 1
            self.__current_atom = 1

            try:
                return list(self.__chains[self.__current_chain].residues())[self.__current_residue - 1]
            except:
                raise StopIteration

class AtomsInStructureIterator:
    def __init__(self, strctr: Structure):
        self.__chains = list(strctr.chains())
        self.__current_chain = 0
        self.__current_chain_it = AtomsInChainIterator(self.__chains[self.__current_chain])

    def __next__(self):

        try:
            return self.__current_chain_it.__next__()

        except:
            try:
                self.__current_chain += 1
                self.__current_chain_it = AtomsInChainIterator(self.__chains[self.__current_chain])
                return self.__current_chain_it.__next__()

            except:
                raise StopIteration


@dataclass
class Structure:
    id_code: str
    __chains: Dict[str, Chain] = field(default_factory=dict)

    def get_chain(self, chain_id: str):
        return self.__chains.get(chain_id, None)

    def add_chain(self, chain: Chain):
        self.__chains[chain.code] = chain

    def chains(self):
        return self.__chains.values()

    def atoms(self):
        return Iterable(AtomsInStructureIterator(self))

    # ta metoda ma zwracać iterator po atomach struktury
    def residues(self):
        return Iterable(ResiduesInStructureIterator(self))
        # return ResiduesInStructureIterator(self)

@dataclass
class Chain:
    code: str
    __residues: Dict[str, Residue] = field(default_factory=dict)

    # chcemy żeby __residues było słownikiem
    # więc piszemy __resdues = {},
    # ale jeśli się tak zrobi to wszystkie obiekty tej klasy dostaną tej sam słownik
    # ale jak robimy __residues = field to możemy traktować to jak maker i możemy traktować
    # to jak każdy różny słownik
    # de facto jest to pole statyczne i

    def get_residue(self, res_seq: int, i_code: str):
        key = str(res_seq) + i_code
        return self.__residues.get(key, None)

    def add_residue(self, res: Residue):
        key = str(res.res_seq) + res.i_code
        self.__residues[key] = res

    def residues(self):
        return self.__residues.values()

    def atoms(self):
        return Iterable(AtomsInChainIterator(self))


@dataclass
class Residue:
    res_name: str
    res_seq: int
    i_code: str
    __atoms: list[Atom] = field(default_factory=list)

    def get_atom(self, serial):
        return self.__atoms[serial - 1]

    def add_atom(self, atom):
        self.__atoms.append(atom)

    def ca(self):
        """Returns the alpha carbon of this residue or None when not present"""
        return next((a for a in self.__atoms if a.name == " CA "), None)

    def atoms(self):
        return self.__atoms

    def __str__(self):
        return f"{self.res_name} {self.res_seq}{self.i_code}"


@dataclass
class Atom:
    serial: int
    name: str
    x: float
    y: float
    z: float

    def distance_to(self, a):
        d2 = (self.x - a.x) * (self.x - a.x)
        d2 += (self.y - a.y) * (self.y - a.y)
        return math.sqrt(d2 + (self.z - a.z) * (self.z - a.z))


def read_pdb_content(code, input_lines):
    strctr = Structure(code)

    for line in input_lines:
        if not line.startswith("ATOM") and not line.startswith("HETAT"): continue
        name = line[12:16]
        serial = int(line[6:11].strip())
        res_name = line[17:20]
        res_seq = int(line[22:26].strip())
        i_code = line[26]
        chain_id = line[21]
        x = float(line[30:38].strip())
        y = float(line[38:46].strip())
        z = float(line[46:54].strip())
        chain = strctr.get_chain(chain_id)
        if chain is None:
            chain = Chain(chain_id)
            strctr.add_chain(chain)
        resid = chain.get_residue(res_seq, i_code)
        if resid is None:
            resid = Residue(res_name, res_seq, i_code)
            chain.add_residue(resid)
        atom = Atom(serial, name, x, y, z)
        resid.add_atom(atom)

    return strctr


class Iterable:
    def __init__(self, iterator):
        self.__iterator = iterator

    def __iter__(self):
        return self.__iterator


if __name__ == "__main__":
    strctr = read_pdb_content("2GB1", open("2gb1.pdb"))
    for c in strctr.chains():
        print(c.code)

    chain_A = strctr.get_chain("A")
    for ri, rj in itertools.combinations(chain_A.residues(), 2):
        print(ri, rj, ri.ca().distance_to(rj.ca()))
