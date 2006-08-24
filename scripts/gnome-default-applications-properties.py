#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-default-applications-properties'
window_title = 'Preferred Applications'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)
	
click (window_title, 'btnClose')

a11y_test_shutdown ()
