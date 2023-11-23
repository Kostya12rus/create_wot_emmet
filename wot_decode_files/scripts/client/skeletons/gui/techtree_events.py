# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/techtree_events.py
from Event import Event

class ITechTreeEventsListener(object):
    onEventsUpdated = None
    onSettingsChanged = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    @property
    def actions(self):
        raise NotImplementedError

    def getUserName(self, actionID):
        raise NotImplementedError

    def getVehicles(self, nationID=None):
        raise NotImplementedError

    def setNationViewed(self, nationID):
        raise NotImplementedError

    def getNations(self, unviewed=False, actionID=None):
        raise NotImplementedError

    def getTimeTillEnd(self, actionID):
        raise NotImplementedError

    def getFinishTime(self, actionID):
        raise NotImplementedError

    def hasActiveAction(self, vehicleCD, nationID=None):
        raise NotImplementedError

    def getActiveAction(self, vehicleCD=None, nationID=None):
        raise NotImplementedError