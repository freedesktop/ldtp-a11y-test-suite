#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'banshee'
window_title = '*Banshee Music Player'

a11y_test_init (program_name)

time.sleep (20)
guiexist (window_title)

a11y_scan_window (window_title)

selectmenuitem (window_title, 'mnuMusic;mnuImportMusic')
a11y_scan_dialog ('dlgImportMusictoLibrary', 'btnCancel')

selectmenuitem (window_title, 'mnuMusic;mnuOpenLocation')
a11y_scan_dialog ('dlgOpenLocation', 'btnCancel')

selectmenuitem (window_title, 'mnuEdit;mnuPlugins')
a11y_scan_dialog ('dlgBansheePlugins', 'btnClose')

selectmenuitem (window_title, 'mnuEdit;mnuPreferences')
if (objectexist ('*Preferences', 'btnCancel')):
    a11y_scan_dialog ('*Preferences', 'btnCancel')
else:
    a11y_scan_dialog ('*Preferences', 'btnClose')

selectmenuitem (window_title, 'mnuView;mnuColumns')
a11y_scan_dialog ('*ChooseColumns', 'btnClose')

if (objectexist (window_title, 'mnuView;mnuLoggedEventsViewer')):
    selectmenuitem (window_title, 'mnuView;mnuLoggedEventsViewer')
    a11y_scan_dialog ('*LogViewer', 'btnClose')

if (objectexist (window_title, 'mnuHelp;mnuVersionInformation')):
    selectmenuitem (window_title, 'mnuHelp;mnuVersionInformation')
    a11y_scan_dialog ('*AssemblyVersionInformation', 'btnClose')
else:
    selectmenuitem (window_title, 'mnuHelp;mnuAbout')
    a11y_scan_dialog ('*About*Banshee', 'btnClose')

selectmenuitem (window_title, 'mnuMusic;mnuQuit')

a11y_test_shutdown ()

