
python_DATA = A11yTestUtils.py
pyc_DATA = $(python_DATA:.py=.pyc)
pycdir = $(pythondir)

%.pyc: %.py
	$(PYTHON) -c "import py_compile; py_compile.compile ('$<', '$@')"

EXTRA_DIST = $(python_DATA)

CLEANFILES =	\
	$(pyc_DATA)

MAINTAINERCLEANFILES =		\
	Makefile.in
