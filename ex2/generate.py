import numpy as np
import random
from math import cos, sin, sqrt


class Atom:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		l = [1, 2]
		w = [10, 1]
		p = random.choices(l, weights=w)[0]
		self.type = p
		v0 = 0   #初速の大きさ
		z = random.random()*2.0-1
		s = random.random()*3.14*2.0
		self.vx = v0*sqrt(1.0-z**2)*cos(s)
		self.vy = v0*sqrt(1.0-z**2)*sin(s)
		self.vz = v0*z


#密度から格子数を計算　L: シミュレーションボックス　rho: 密度
def get_lattice_number(L, rho):
	m = np.floor((L**3 * rho / 4.0)**(1.0 / 3.0))
	drho1 = np.abs(4.0 * m **3 / L**3 - rho)
	drho2 = np.abs(4.0 * (m + 1)**3 / L**3 - rho)
	if drho1 < drho2:
		return m
	else:
		return m + 1


def add_ball(atoms, L, rho):
	m = int(get_lattice_number(L, rho))  #r = 8
	s = 1.7     #単位格子の一辺の長さ
	h = 0.5 * s
	for ix in range(0, m):
		for iy in range(0, m):
			for iz in range(0, m):
				x = ix * s
				y = iy * s
				z = iz * s
				atoms.append(Atom(x, y, z))
				atoms.append(Atom(x, y+h, z+h))
				atoms.append(Atom(x+h, y, z+h))
				atoms.append(Atom(x+h, y+h, z))


def save_file(filename, atoms):
	with open(filename, "w") as f:
		f.write("Position Data\n\n")
		f.write("{} atoms\n".format(len(atoms)))
		f.write("2 atom types\n\n")
		f.write("0.00 17.00 xlo xhi\n")
		f.write("0.00 17.00 ylo yhi\n")
		f.write("0.00 17.00 zlo zhi\n")
		f.write("\n")
		f.write("Atoms\n\n")
		for i, a in enumerate(atoms):
			f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
		f.write("\n")
		f.write("Velocities\n\n")
		for i, a in enumerate(atoms):
			f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
	print("Generated {}".format(filename))


atoms = [] 

add_ball(atoms, 17, 0.8)

save_file("decomp.atoms", atoms)
