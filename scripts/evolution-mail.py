#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'evolution'
window_title = 'Evolution*'

a11y_test_init (program_name)

guiexist (window_title)

a11y_scan_window (window_title)

# Close the main window
selectmenuitem (window_title, 'mnuFile;mnuQuit')

a11y_test_shutdown ()

