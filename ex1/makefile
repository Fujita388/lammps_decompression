all: decomp.lammpstrj

decomp.lammpstrj:
	python3 generate.py
	/home/Fujita388/github/lammps/src/lmp_serial < decomp.input

rescale: 
	python3 rescale.py > rescale.atoms
	/home/Fujita388/github/lammps/src/lmp_serial < rescale.input

clean: 
	rm *.lammpstrj *.atoms 


