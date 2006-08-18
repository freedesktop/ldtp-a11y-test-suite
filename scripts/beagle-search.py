#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'beagle-search'
window_title = '*Search'

a11y_test_init (program_name)
guiexist (window_title)

a11y_scan_window (window_title)

#This doesn't seem to work
#selectmenuitem (window_title, 'mnuSearch')
#__check_dialog ('*Preferences', 'btnClose')

#selectmenuitem (window_title, 'mnuSearch;mnuQuit')

a11y_test_shutdown ()

os.system ('pkill -9 ' + program_name)
