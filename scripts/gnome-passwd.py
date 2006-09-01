#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-passwd'
window_title = 'Change Password'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)
	
click (window_title, 'btnCancel')

a11y_test_shutdown ()
