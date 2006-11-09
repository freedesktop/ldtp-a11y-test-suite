#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *
from A11yTestUtils import *

program_name = 'gnome-panel'

a11y_test_init (program_name, '', 1)

panel_titles = [
    'frmBottomExpandedEdgePanel',
    'frmBottomEdgePanel',
    'frmBottomCenteredPanel',
    'frmRightExpandedEdgePanel',
    'frmRightEdgePanel',
    'frmRightCenteredPanel',
    'frmTopExpandedEdgePanel',
    'frmTopEdgePanel',
    'frmTopCenteredPanel',
    'frmLeftExpandedEdgePanel',
    'frmLeftEdgePanel',
    'frmLeftCenteredPanel'
    ]

for window_title in panel_titles:
    if (guiexist (window_title)):
        a11y_scan_window (window_title)
    else:
        continue

a11y_test_shutdown ()
