# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/EditUtils.py
import BigWorld, GUI, Math, ResMgr

def setup():
    BigWorld.camera(BigWorld.CursorCamera())
    BigWorld.setCursor(GUI.mcursor())
    GUI.mcursor().visible = True


def clearAll():
    while len(GUI.roots()):
        GUI.delRoot(GUI.roots()[0])


def clone(component):
    ResMgr.purge('gui/temp_clone.gui', True)
    component.save('gui/temp_clone.gui')
    return GUI.load('gui/temp_clone.gui')


weatherWindow = None

def weather():
    global weatherWindow
    setup()
    weatherWindow = GUI.load('gui/weather_window.gui')
    GUI.addRoot(weatherWindow)
    return weatherWindow


def saveWeather():
    if weatherWindow:
        weatherWindow.save('gui/weather_window.gui')