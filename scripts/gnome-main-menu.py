#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'main-menu'
window_title = 'frmBottomExpandedEdgePanel'

a11y_test_init (program_name, None, 1)

if (guiexist (window_title)):
    if (objectexist (window_title, 'tbtnComputer')):
        press (window_title, 'tbtnComputer')
        guiexist ('Main Menu')
        a11y_scan_window ('Main Menu')
        press (window_title, 'tbtnComputer')
    else:
        print "Main Menu applet not found on panel"
else:
    print "Panel not found"

a11y_test_shutdown ()
