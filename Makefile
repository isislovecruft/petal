all:
	swig -python -c -o _petal_pgp.c petal.i
	python setup.py build_ext --inplace

etags:
	find . -regextype posix-extended -regex ".+\.([ch]|py)" | xargs etags
