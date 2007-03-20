#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'abiword'
window_title = 'Untitled1'

a11y_test_init (program_name)

while (guiexist (window_title) != 1):
    continue;

a11y_scan_window (window_title)
	
selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()
