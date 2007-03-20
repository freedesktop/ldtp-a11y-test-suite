#!/usr/bin/python

import string, sys, os

from ldtp import *
from ldtputils import *
from A11yTestUtils import *

path = os.environ['PATH'];
os.environ['PATH'] = path + ':/opt/gnome/lib/evolution-webcal:/usr/lib/evolution-webcal';
path = os.environ['PATH'];

log_name = 'evolution-webcal'
program_name = 'evolution-webcal'

for dir in string.split (path, ':'):
    program = dir + '/evolution-webcal';
    if (os.path.isfile (program)):
        program_name = program;

window_title = 'Subscribe to Calendar'

calendar_url = 'webcal://icalx.com/public/prepgroove/200732NASCAR32Nextel32Cup32Series.ics'

a11y_test_init (program_name, calendar_url, 0, log_name)

while (guiexist (window_title) != 1):
    continue;

a11y_scan_window (window_title)
	
click (window_title, 'btnCancel')

a11y_test_shutdown ()
