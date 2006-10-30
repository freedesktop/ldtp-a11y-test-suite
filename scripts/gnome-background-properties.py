#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-background-properties'
window_title = 'Desktop Background Preferences'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)

if (objectexist (window_title, 'btnFinish')):
        click (window_title, 'btnFinish')
else:
        click (window_title, 'btnClose')
        

a11y_test_shutdown ()
