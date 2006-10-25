#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-volume-properties'
window_title = 'Drives and Media Preferences'

a11y_test_init (program_name)

waittillguiexist (window_title)

a11y_scan_window (window_title)
	
click (window_title, 'btnClose')

a11y_test_shutdown ()
