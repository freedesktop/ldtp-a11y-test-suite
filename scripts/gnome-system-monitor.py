#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-system-monitor'
window_title = '*Monitor'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)
	
selectmenuitem (window_title, 'mnuEdit;mnuPreferences')
a11y_scan_dialog ('*Pref*', 'btnClose')

selectmenuitem (window_title, 'mnuHelp;mnuAbout')
a11y_scan_dialog ('*About*', 'btnClose')

selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()
