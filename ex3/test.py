#atoms_idとbond_idの紐付け
def Atoms(atoms_file, atoms_id):
	bond_list = []
	with open(atoms_file, "r") as f:
		atoms_data = f.readlines()
	for i in range(4000):
		bond_id = atoms_data[i+14].split()[1]
		bond_list.append(bond_id)
	print(bond_list[atoms_id-1])


Atoms("decomp.atoms", 11)

