


def readdump(atoms_file):
	with open(atoms_file, "r") as f:
		atoms_data = f.readlines()
	print(atoms_data[3])
	for i, line in enumerate(atoms_data):
		if "Bonds" in line:
			print(atoms_data[i])
			while len(atoms_data) > i+2:
				bond = atoms_data[i+2].split()
				print(bond[0] + ' ' + bond[1] + ' ' + bond[2] + ' ' + bond[3])
				i += 1



readdump("decomp.atoms")



