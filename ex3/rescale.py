#decomp.aotmsとdecomp.lammpstrjを読み込んで座標を1.05倍にし、rescale.atomsをはく
#atom_id, bond_id, atom_type, x, y, z
#bond_idをatom_idに紐づける必要あり
#[bond_id]のリストを作って、インデックスを(atom_id)-1にする。



def readdump(atoms_file, dump_file):
	#atomsのファイルを読み込み
	with open(atoms_file, "r") as f:
		atoms_data = f.readlines()
	#dumpファイルを読み込み
	with open(dump_file, "r") as f:
		dump_data = f.readlines()
	bond_list = []  #bond_idのリスト(インデックスがatoms_id)
	group = []  #ダンプファイルにおけるグループの始まりのインデックスの配列
	for i, line in enumerate(dump_data):
		if "ITEM: TIMESTEP" in line:
			group.append(i)
	num_atoms = int(dump_data[3])  #atomの数
	l = dump_data[group[-1]+5]  
	L = float(l.split()[1])  #シミュレーションボックスのサイズ
	#atoms_idとbond_idの対応
	for i in range(num_atoms):
		bond_id  = atoms_data[i+14].split()[1]
		bond_list.append(bond_id)
	print("Position Data\n")
	print(str(num_atoms) + " atoms")
	print(atoms_data[3])
	print("2 atom types")
	print("1 bond types\n")
	print("0.00 " + str(1.05*L) + " xlo xhi")
	print("0.00 " + str(1.05*L) + " ylo yhi")
	print("0.00 " + str(1.05*L) + " zlo zhi\n")
	print("Atoms\n")
	for i in range(num_atoms):
		position = dump_data[group[-1]+9+i]  #最後のグループの座標dataの先頭
		atoms_id = int(position.split()[0])
		atoms_type = int(position.split()[1])
		x = float(position.split()[2])
		y = float(position.split()[3])
		z = float(position.split()[4])
		x = 1.05 * L * x
		y = 1.05 * L * y
		z = 1.05 * L * z
		print(atoms_id, bond_list[atoms_id-1], atoms_type, x, y, z)
	print("\n")
	print("Velocities\n")
	for i in range(num_atoms):
		atoms_id = i+1
		print(atoms_id, "0.0 0.0 0.0")
	print('\n')
	for i, line in enumerate(atoms_data):
		if "Bonds" in line:
			print(atoms_data[i])
			while len(atoms_data) > i+2:
				bond = atoms_data[i+2].split()
				print(bond[0] + ' ' + bond[1] + ' ' + bond[2] + ' ' + bond[3])
				i += 1


readdump("decomp.atoms", "decomp.lammpstrj")
