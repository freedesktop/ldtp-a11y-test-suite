#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

os.environ['GTK_MODULES'] = 'gail:atk-bridge'
os.environ['GNOME_ACCESSIBILITY'] = '1'

program_name = 'realplay'
window_title = 'RealPlayer'

a11y_test_init (program_name)
a11y_scan_window (window_title)

selectmenuitem (window_title, 'mnuFile;mnuOpenFile')
a11y_scan_dialog ('*files', 'btnCancel')

selectmenuitem (window_title, 'mnuFile;mnuOpenLocation')
a11y_scan_dialog ('dlgOpenLocation', 'btnCancel')

selectmenuitem (window_title, 'mnuFile;mnuClipProperties;mnuViewClipInfo')
a11y_scan_dialog ('dlgClipDetails', 'btnClose')

selectmenuitem (window_title, 'mnuTools;mnuPlugins')
a11y_scan_dialog ('dlgPlugins', 'btnClose')

selectmenuitem (window_title, 'mnuTools;mnuPreferences')
a11y_scan_dialog ('dlgPreferences', 'btnOK')

selectmenuitem (window_title, 'mnuTools;mnuPlaybackStatistics')
a11y_scan_dialog ('*Statistics', 'btnClose')

selectmenuitem (window_title, 'mnuFavorites;mnuManageFavorites')
a11y_scan_dialog ('*Favorites', 'btnClose')

selectmenuitem (window_title, 'mnuHelp;mnuAbout')
a11y_scan_dialog ('dlgAboutRealPlayer', 'btnClose')

selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()
