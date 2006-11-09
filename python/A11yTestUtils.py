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
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of version 2 of the GNU General Public License
#  as published by the Free Software Foundation
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Street #330, Boston, MA 02111-1307, USA.
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
    utfname = componentName.encode ('utf8')
    properties = getobjectinfo (windowName, componentName)
    f.write ('<td>' + errorString + '</td>\n')
    f.write ('<td class=\"widgetname\">' + utfname + '</td>\n')
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

def a11y_find_panel_with_applet (appletName):
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

    for panel_title in panel_titles:
        if (guiexist (panel_title)):
            if (objectexist (panel_title, appletName)):
                return panel_title
            else:
                continue
        else:
            continue

    return None

def a11y_test_init (programName, argumentList = '', noLaunch = 0):
    global f
    ldtp.setlocale ('en_US.UTF-8')
    f = open (programName + '.html', 'w')
    f.write ('<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\">')
    f.write ('<html>\n')
    f.write ('<head>\n')
    f.write ('<title>' + programName + ' Accessibility Test Summary</title>\n')
    f.write ('<style type=\"text/css\">@import url(report.css);</style>')
    f.write ('</head>\n')
    f.write ('<body>\n')
    if (noLaunch == 0):
        if (argumentList != ''):
            launchapp (programName + ' ' + argumentList, 1)
        else:
            launchapp (programName, 1)

def a11y_test_shutdown ():
    f.write ('</body>\n')
    f.write ('</html>\n')
    f.close ()
