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

selectmenuitem (window_title, 'mnuXtns;mnuPlug-InBrowser')
a11y_scan_dialog ('dlgPlug-InBrowser', 'btnClose')

selectmenuitem (window_title, 'mnuXtns;mnuProcedureBrowser')
a11y_scan_dialog ('dlgProcedureBrowser', 'btnClose')

selectmenuitem (window_title, 'mnuXtns;mnuUnitEditor')
a11y_scan_dialog ('dlgUnitEditor', 'btnClose')

# LDTP BUG: Help and Help are the same, and LDTP uses a hash table...
#selectmenuitem (window_title, 'mnuHelp;mnuHelp')
#a11y_scan_dialog ('wndGIMPHelpBrowser', 'btnClose')

selectmenuitem (window_title, 'mnuHelp;mnuTipoftheDay')
a11y_scan_dialog ('frmGIMPTipoftheDay', 'btnClose')

selectmenuitem (window_title, 'mnuXtns;mnuScript-Fu;mnuButtons;mnuRoundButton')
a11y_scan_dialog ('dlgScript-Fu:RoundButton', 'btnOK')

# LDTP BUG: Need to wait for previous operations to complete
# GIMP can't run multiple script-fu scripts at the same time
#selectmenuitem (window_title, 'mnuXtns;mnuScript-Fu;mnuButtons;mnuSimpleBeveledButton')
#a11y_scan_dialog ('dlgScript-Fu:SimpleBeveledButton', 'btnOK')

# Close GIMP (Should wait for previous operations to complete)
selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()

