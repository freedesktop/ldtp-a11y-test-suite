#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-theme-manager'
window_title = 'Theme Preferences'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)
	
click (window_title, 'btnInstallTheme')
a11y_scan_dialog ('dlgThemeInstallation', 'btnCancel')

click (window_title, 'btnThemeDetails')
a11y_scan_dialog ('dlgThemeDetails', 'btnClose')

click (window_title, 'btnClose')

a11y_test_shutdown ()
