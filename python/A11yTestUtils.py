#!/usr/bin/env python

#############################################################################
#
#  Accessibility Evaluation Test Utils
# 
#  Author:
#     Rodney Dawes <dobey@novell.com>
# 
#  Copyright 2006 Novell, Inc.
# 
#############################################################################

from ldtp import *
from ldtputils import *

f = None;

def __has_label (windowName, componentName):
    properties = getobjectinfo (windowName, componentName)
    for prop in properties:
	if prop == 'label':
	    return 1
	elif prop == 'label_by':
	    return 1
	continue
    return 0

def __has_description (windowName, componentName):
    properties = getobjectinfo (windowName, componentName)
    for prop in properties:
	if prop == 'description':
	    return 1
	continue
    return 0
    
def __print_properties (errorString, windowName, componentName):
    properties = getobjectinfo (windowName, componentName)
    f.write ('<td>' + errorString + '</td>\n')
    f.write ('<td class=\"widgetname\">' + componentName + '</td>\n')
    propValue = getobjectproperty (windowName, componentName, 'class')
    f.write ('<td>' + propValue + '</td>\n')
    propValue = getobjectproperty (windowName, componentName, 'parent')
    f.write ('<td>' + propValue + '</td>\n')

def a11y_scan_dialog (windowName, closeButton):
    waittillguiexist (windowName)
    objlist = getobjectlist (windowName)
    f.write ('<table summary=\"\">\n')
    f.write ('<caption>' + windowName + '</caption>')
    f.write ('<tr>\n')
    f.write ('<th>Issue</th>')
    f.write ('<th>Widget</th><th>Widget Class</th><th>Parent Widget</th>\n')
    f.write ('</tr>')
    has_label = 0
    for obj in objlist:
	if hasstate (windowName, obj, state.FOCUSABLE) == 1:
	    if __has_label (windowName, obj) == 0:
		f.write ('<tr>\n')
		__print_properties ('Missing Name', windowName, obj)
		f.write ('</tr>\n')
	    if __has_description (windowName, obj) == 0:
		f.write ('<tr>\n')
		__print_properties ('Missing Description', windowName, obj)
		f.write ('</tr>\n')
    f.write ('</table>\n')
    click (windowName, closeButton)

def a11y_scan_window (windowName):
    waittillguiexist (windowName)
    objlist = getobjectlist (windowName)
    f.write ('<table summary=\"\">\n')
    f.write ('<caption>' + windowName + '</caption>')
    f.write ('<tr>\n')
    f.write ('<th>Issue</th>')
    f.write ('<th>Widget</th><th>Widget Class</th><th>Parent Widget</th>\n')
    f.write ('</tr>')
    has_label = 0
    for obj in objlist:
	if hasstate (windowName, obj, state.FOCUSABLE) == 1:
	    if __has_label (windowName, obj) == 0:
		f.write ('<tr>\n')
		__print_properties ('Missing Name', windowName, obj)
		f.write ('</tr>\n')
	    if __has_description (windowName, obj) == 0:
		f.write ('<tr>\n')
		__print_properties ('Missing Description', windowName, obj)
		f.write ('</tr>\n')
    f.write ('</table>\n')

def a11y_test_init (programName):
    global f
    f = open (programName + '.html', 'w')
    f.write ('<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\">')
    f.write ('<html>\n')
    f.write ('<head>\n')
    f.write ('<title>' + programName + ' Accessibility Test Summary</title>\n')
    f.write ('<style type=\"text/css\">@import url(report.css);</style>')
    f.write ('</head>\n')
    f.write ('<body>\n')
    launchapp (programName, 1)

def a11y_test_shutdown ():
    f.write ('</body>\n')
    f.write ('</html>\n')
    f.close ()