#!/usr/bin/python
# The above must always be the first line in the script

# Import a bunch of modules, so everything will work.
# This block of imports can be copy-pasted into new scripts.
import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

# The program_name is the executable binary name that you will find in
# the $PATH (/usr/bin, /opt/gnome/bin, etc...).
# The window_title is the unique window title string that the main window
# for the application will have at startup, this can be glob'd, like below
program_name = 'yelp'
window_title = '*Topics'

# Initialize the test run, so that we can log the data to our HTML file
a11y_test_init (program_name)

# Make sure the window exists. This may take a while to occur for some
# applications, and a time.sleep(10) or similar may need to be inserted
# prior to guiexist ()
guiexist (window_title)

# Scan the main window. If the application's main window is a dialog, we
# still want to use this call, as we need to call a11y_test_shutdown below,
# and there may be other windows or dialogs within the application that we
# wish to scan
a11y_scan_window (window_title)

# Select the Edit:Preferences menu item, and scan the dialog that it opens
# We use a11y_scan_dialog here, as we want to scan and close it
# If there are any items within the dialog that need to be checked as well,
# then a11y_scan_window should be used again, and one would have to call
# click ('*Preferences*', 'btnClose') afterward, in the case below
selectmenuitem (window_title, 'mnuEdit;mnuPreferences')
a11y_scan_dialog ('*Preferences*', 'btnClose')

selectmenuitem (window_title, 'mnuBookmarks;mnuEditBookmarks')
a11y_scan_dialog ('dlgBookmarks', 'btnClose')

# Close the main window as we are done scanning
selectmenuitem (window_title, 'mnuFile;mnuClose*')

# Shutdown the a11y test suite, and close the HTML log file
a11y_test_shutdown ()

