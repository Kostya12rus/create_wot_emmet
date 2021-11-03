# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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