#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gimp'
window_title = 'The GIMP'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)

selectmenuitem (window_title, 'mnuFile;mnuNew')
a11y_scan_dialog ('dlgCreateaNewImage', 'btnOK')
# The canvas window apparently is not accessible :(
#a11y_scan_window ('wndUntitled-*')

selectmenuitem (window_title, 'mnuFile;mnuOpenLocation')
a11y_scan_dialog ('dlgOpenLocation', 'btnCancel')

selectmenuitem (window_title, 'mnuFile;mnuAcquire;mnuScreenShot')
a11y_scan_dialog ('dlgScreenShot', 'btnCancel')

#selectmenuitem (window_title, 'mnuFile;mnuPreferences')
#a11y_scan_dialog ('dlgPreferences', 'btnCancel')

selectmenuitem (window_title, 'mnuXtns;mnuModuleManager')
a11y_scan_dialog ('dlgModuleManager', 'btnClose')

#selectmenuitem (window_title, 'mnuXtns;mnuPluginBrowser')
#a11y_scan_dialog ('dlgPluginBrowser', 'btnClose')

selectmenuitem (window_title, 'mnuXtns;mnuProcedureBrowser')
a11y_scan_dialog ('dlgProcedureBrowser', 'btnClose')

selectmenuitem (window_title, 'mnuXtns;mnuUnitEditor')
a11y_scan_dialog ('dlgUnitEditor', 'btnClose')

#selectmenuitem (window_title, 'mnuHelp;mnuHelp')
#a11y_scan_dialog ('wndGIMPHelpBrowser', 'btnClose')

#selectmenuitem (window_title, 'mnuHelp;mnuTipoftheDay')
#a11y_scan_dialog ('dlgGIMPTipoftheDay', 'btnClose')

# Close GIMP
selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()

