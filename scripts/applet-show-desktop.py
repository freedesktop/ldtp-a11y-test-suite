#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'applet-show-desktop'
applet_title = 'Show Desktop Button'

a11y_test_init (program_name, None, 1)

window_title = a11y_find_panel_with_applet (applet_title)

if (window_title != None):
    print applet_title + " found on " + window_title
else:
    print "No panel found with " + applet_title

a11y_test_shutdown ()
