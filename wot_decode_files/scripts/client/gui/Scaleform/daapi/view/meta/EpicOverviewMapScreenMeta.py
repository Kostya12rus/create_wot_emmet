# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicOverviewMapScreenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicOverviewMapScreenMeta(BaseDAAPIComponent):

    def as_setKeyBindingsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setKeyBindings(data)

    def as_updateLaneButtonNamesS(self, west, center, east):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLaneButtonNames(west, center, east)