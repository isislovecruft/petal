all:
	swig -python -c -o _petal_pgp.c petal.i
	python setup.py build_ext --inplace

