#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gaim'
window_title = 'Login'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)

#click (window_title, 'btnAccounts')
#a11y_scan_dialog ('dlgAccounts', 'btnClose')

#click (window_title, 'btnPreferences')
#a11y_scan_dialog ('dlgPreferences', 'btnClose')

#selectmenuitem (window_title, 'mnuFile;mnuClose*')

a11y_test_shutdown ()

