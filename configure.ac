dnl Process this file with autoconf to produce a configure script.
AC_PREREQ(2.52)

AC_INIT([a11y-test-suite], [2.11.0])
AC_CONFIG_SRCDIR(HACKING)
AC_COPYRIGHT([Copyright 2006 Novell, Inc.])

AM_INIT_AUTOMAKE
AM_MAINTAINER_MODE

AC_MSG_CHECKING([python site path])
pythonsitedir="`./find-python-path.py`"
pythondir="\${libdir}/${pythonsitedir}"
AC_MSG_RESULT([$pythondir])
AC_SUBST(pythondir)

AC_CONFIG_FILES([
Makefile
python/Makefile
scripts/Makefile
])

AC_OUTPUT
