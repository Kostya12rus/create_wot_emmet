# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/hangar/__init__.py
import pointcuts as _pointcuts

def configure_pointcuts(config):
    _pointcuts.DisableTankServiceButtons(config)
    _pointcuts.ShowMiniclientInfo()
    _pointcuts.TankHangarStatus(config)
    _pointcuts.TankModelHangarVisibility(config)
    _pointcuts.EnableCrew(config)
    _pointcuts.ChangeLobbyMenuTooltip()