#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'banshee'
window_title = '*Banshee Music Player'

a11y_test_init (program_name)
guiexist (window_title)

a11y_scan_window (window_title)

selectmenuitem (window_title, 'mnuMusic;mnuImportMusic')
a11y_scan_dialog ('dlgImportMusictoLibrary', 'btnCancel')

selectmenuitem (window_title, 'mnuMusic;mnuOpenLocation')
a11y_scan_dialog ('dlgOpenLocation', 'btnCancel')

selectmenuitem (window_title, 'mnuEdit;mnuPlugins')
a11y_scan_dialog ('dlgBansheePlugins', 'btnClose')

selectmenuitem (window_title, 'mnuEdit;mnuPreferences')
a11y_scan_dialog ('*Preferences', 'btnCancel')

selectmenuitem (window_title, 'mnuView;mnuColumns')
a11y_scan_dialog ('*ChooseColumns', 'btnClose')

selectmenuitem (window_title, 'mnuView;mnuLoggedEventsViewer')
a11y_scan_dialog ('*LogViewer', 'btnClose')

selectmenuitem (window_title, 'mnuHelp;mnuVersionInformation')
a11y_scan_dialog ('*AssemblyVersionInformation', 'btnClose')

selectmenuitem (window_title, 'mnuMusic;mnuQuit')

a11y_test_shutdown ()

