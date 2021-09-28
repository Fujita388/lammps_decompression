

def readdump(filename):
	with open(filename, "r") as f:
		data = f.readlines()
	group = []  #グループの始まりのインデックスの配列
	for i, line in enumerate(data):
		if "ITEM: TIMESTEP" in line:
			group.append(i)
	num_atoms = int(data[3])  #atomの数
	l = data[group[-1]+5]  
	L = float(l.split()[1])  #シミュレーションボックスのサイズ
	print("Position Data\n")
	print(str(num_atoms) + " atoms")
	print("1 atom types\n")
	print("0.00 " + str(1.05*L) + " xlo xhi")
	print("0.00 " + str(1.05*L) + " ylo yhi")
	print("0.00 " + str(1.05*L) + " zlo zhi\n")
	print("Atoms\n")
	for i in range(num_atoms):
		position = data[group[-1]+9+i]  #最後のグループの座標dataの先頭
		atoms_id = int(position.split()[0])
		atoms_type = int(position.split()[1])
		x = float(position.split()[2])
		y = float(position.split()[3])
		z = float(position.split()[4])
		x = 1.05 * L * x
		y = 1.05 * L * y
		z = 1.05 * L * z
		print(atoms_id, atoms_type, x, y, z)
	print("\n")
	print("Velocities\n")
	for i in range(num_atoms):
		atoms_id = i+1
		print(atoms_id, " 0.0 0.0 0.0")


readdump("decomp.lammpstrj")


