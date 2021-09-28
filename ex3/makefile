all: bond.lammpstrj

bond.lammpstrj:
	python3 generate.py
	/home/Fujita388/github/lammps/src/lmp_serial < decomp.input

rescale: 
	python3 rescale.py > rescale.atoms
	/home/Fujita388/github/lammps/src/lmp_serial < rescale.input

test:
	python3 test.py > test.atoms

clean:
	rm *.atoms *.lammpstrj log.lammps 
