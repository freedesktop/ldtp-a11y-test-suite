#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'banshee'
window_title = '*Banshee*'

a11y_test_init (program_name)
guiexist (window_title)

a11y_scan_window (window_title)

selectmenuitem (window_title, 'mnuEdit;mnuPreferences')
a11y_scan_dialog ('*Preferences', 'btnClose')

selectmenuitem (window_title, 'mnuMusic;mnuQuit')

a11y_test_shutdown ()

