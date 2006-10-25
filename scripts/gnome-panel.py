#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-panel'
window_title = 'Bottom Expanded Edge Panel'

a11y_test_init (program_name, '', 1)

guiexist (window_title)

a11y_scan_window (window_title)

a11y_test_shutdown ()
