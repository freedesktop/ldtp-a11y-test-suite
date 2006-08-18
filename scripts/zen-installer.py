#!/usr/bin/python

import string, sys, os
from ldtp import *
from ldtputils import *

os.environ['GTK_MODULES'] = 'gail:atk-bridge'
os.environ['GNOME_ACCESSIBILITY'] = '1'

program_name = 'zen-installer'
window_title = '*Install*'

def __has_label (windowName, componentName):
    properties = getobjectinfo (windowName, componentName)
    for prop in properties:
	if prop == 'label':
	    return 1
	elif prop == 'label_by':
	    return 1
	continue
    return 0

def __print_properties (windowName, componentName):
    properties = getobjectinfo (windowName, componentName)
    for prop in properties:
	propValue = getobjectproperty (windowName, componentName, prop)
	print '\t', prop, ':', propValue

def __check_dialog (windowName, closeButton):
    objlist = getobjectlist (windowName)
    has_label = 0
    for obj in objlist:
	if hasstate (windowName, obj, state.FOCUSABLE) == 1:
	    if __has_label (windowName, obj) == 0:
		print "WARNING:", obj, "has no accessible label defined"
		__print_properties (windowName, obj)
    click (windowName, closeButton)

launchapp (program_name, 1)

guiexist (window_title)

objlist = getobjectlist (window_title)

has_label = 0

for obj in objlist:
    if hasstate (window_title, obj, state.FOCUSABLE) == 1:
	if __has_label (window_title, obj) == 0:
	    print "WARNING:", obj, "has no accessible label defined"
	    __print_properties (window_title, obj)
	
click (window_title, 'btnClose')
