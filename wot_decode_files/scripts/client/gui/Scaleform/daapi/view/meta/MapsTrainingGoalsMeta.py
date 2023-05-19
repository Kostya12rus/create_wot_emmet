# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MapsTrainingGoalsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MapsTrainingGoalsMeta(BaseDAAPIComponent):

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)

    def as_destroyGoalS(self, vehClass):
        if self._isDAAPIInited():
            return self.flashObject.as_destroyGoal(vehClass)

    def as_showHintS(self, hintType, description, time=None):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(hintType, description, time)

    def as_hideHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHint()

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)