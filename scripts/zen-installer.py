#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'zen-installer'
window_title = 'Software Installer'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)

click (window_title, 'btnConfigure')
a11y_scan_window ('frmConfiguration')
time.sleep (1)
click ('frmConfiguration', 'btnAddService')
time.sleep (1)
#a11y_scan_dialog ('dlgAddService', 'btnCancel')
click ('frmConfiguration', 'btnClose')

click (window_title, 'btnClose')

a11y_test_shutdown ()
