#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'application-browser'
window_title = '*Browser'

a11y_test_init (program_name)
guiexist (window_title)

a11y_scan_window (window_title)

#selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()

os.system ('pkill -9 ' + program_name)

