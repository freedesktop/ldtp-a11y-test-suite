#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gedit'
window_title = '*-gedit'

a11y_test_init (program_name)

guiexist (window_title)

# Scan the main window
a11y_scan_window (window_title)

# Scan the various dialogs
selectmenuitem (window_title, 'mnuFile;mnuOpen*')
a11y_scan_dialog ('*Location', 'btnCancel')

selectmenuitem (window_title, 'mnuFile;mnuPage*')
a11y_scan_dialog ('*Page*', 'btnClose')

selectmenuitem (window_title, 'mnuEdit;mnuPreferences')
a11y_scan_dialog ('*Preferences*', 'btnClose')

selectmenuitem (window_title, 'mnuSearch;mnuFind')
a11y_scan_dialog ('*Find*', 'btnClose')

selectmenuitem (window_title, 'mnuSearch;mnuReplace')
a11y_scan_dialog ('*Replace', 'btnClose')

selectmenuitem (window_title, 'mnuSearch;mnuGo*')
a11y_scan_dialog ('*Go*', 'btnClose')

selectmenuitem (window_title, 'mnuTools;mnuCheck*')
a11y_scan_dialog ('*Information*', 'btnOK')

selectmenuitem (window_title, 'mnuTools;mnuSet*')
a11y_scan_dialog ('*anguage', 'btnCancel')

selectmenuitem (window_title, 'mnuTools;mnuDocumentStatistics')
a11y_scan_dialog ('*Statistics', 'btnClose')

selectmenuitem (window_title, 'mnuHelp;mnuAbout')
a11y_scan_dialog ('dlgAboutgedit', 'btnClose')

# Close the app
selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()
