# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AwardGroupsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AwardGroupsMeta(BaseDAAPIComponent):

    def showGroup(self, groupId):
        self._printOverrideError('showGroup')

    def as_setDataS(self, groups):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(groups)

    def as_setTooltipsS(self, tooltips):
        if self._isDAAPIInited():
            return self.flashObject.as_setTooltips(tooltips)

    def as_setSelectedS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelected(id, value)

    def as_setEnabledS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(id, value)