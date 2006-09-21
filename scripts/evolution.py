#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'evolution'
window_title = 'Evolution Setup Assistant'

a11y_test_init (program_name, '-c mail')

#
# This big block of stuff is for the first-run wizard
# it is commented out so that we may 

#guiexist (window_title)
#
#a11y_scan_window (window_title)
#click (window_title, 'btnForward')
#settextvalue (window_title, 'txtEmailAddress', 'user@localhost')
#settextvalue (window_title, 'txtReply-To', 'user@localhost')
#settextvalue (window_title, 'txtOrganization', 'Organization, Inc.')
#time.sleep (1)
#click (window_title, 'btnForward')
#
#time.sleep (1)
#click (window_title, 'btnForward')
#
#time.sleep (2)
#comboselect (window_title, 'cboServerType1', 'Sendmail')
#time.sleep (2)
#lick (window_title, 'btnForward')
#
#settextvalue (window_title, 'txtName', 'Localhost')
#time.sleep (3)
#click (window_title, 'btnForward')
#time.sleep (2)
#click (window_title, 'btnForward')
#time.sleep (2)
#click (window_title, 'btnApply')
#
#time.sleep (2)

# The Main Mail window
guiexist ('*Evolution-*')

a11y_scan_window ('*Evolution-*')

# Scan the preferences dialog
selectmenuitem ('*Evolution-*', 'mnuEdit;mnuPreferences')
a11y_scan_dialog ('dlgEvolutionPreferences', 'btnClose')

# Scan the Mail Filters dialog
selectmenuitem ('*Evolution-*', 'mnuEdit;mnuMessageFilters')
#click ('dlgMessageFilters', 'btnAdd')
#a11y_scan_dialog ('dlgAddRule', 'btnCancel')
a11y_scan_dialog ('dlgMessageFilters', 'btnCancel')

# Scan the Search Folders dialog
selectmenuitem ('*Evolution-*', 'mnuEdit;mnuSearchFolders')
#click ('dlgMessageFilters', 'btnAdd')
#a11y_scan_dialog ('dlgAddRule', 'btnCancel')
a11y_scan_dialog ('dlgSearchFolders', 'btnCancel')

# Scan the Plugin Manager dialog
selectmenuitem ('*Evolution-*', 'mnuEdit;mnuPlugins')
a11y_scan_dialog ('dlgPluginManager', 'btnOK')

# Scan the custom views dialog
selectmenuitem ('*Evolution-*', 'mnuView;mnuCurrentView;mnuDefineViews')
time.sleep (2)
guiexist ('dlgDefineViewsforMail')
click ('dlgDefineViewsforMail', 'btnNew')
a11y_scan_dialog ('dlgDefineNewView', 'btnCancel')
a11y_scan_dialog ('dlgDefineViewsforMail', 'btnClose')

# Scan the subscribe folders dialog
selectmenuitem ('*Evolution-*', 'mnuFolder;mnuSubscriptions')
a11y_scan_dialog ('dlgFolderSubscriptions', 'btnClose')

# Scan the copy folder dialog
selectmenuitem ('*Evolution-*', 'mnuFolder;mnuCopyFolderTo')
a11y_scan_dialog ('dlgSelectfolder', 'btnCancel')

# Scan the folder properties dialog
selectmenuitem ('*Evolution-*', 'mnuFolder;mnuProperties')
a11y_scan_dialog ('dlgFolderProperties', 'btnOK')

# Scan the mail composer
selectmenuitem ('*Evolution-*', 'mnuMessage;mnuComposeNewMessage')
a11y_scan_window ('frmComposeMessage')
selectmenuitem ('frmComposeMessage', 'mnuFile;mnuClose')

# Switch to the Calendar view
selectmenuitem ('*Evolution-*', 'mnuView;mnuWindow;mnuCalendars')

time.sleep (2)
a11y_scan_window ('*Evolution-Calendars')

# Close the main window
selectmenuitem ('*Evolution-Calendars', 'mnuFile;mnuQuit')

a11y_test_shutdown ()

