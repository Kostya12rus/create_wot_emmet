# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesDivisionQualificationMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesDivisionQualificationMeta(BaseDAAPIComponent):

    def as_setQualificationEfficiencyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationEfficiencyData(data)

    def as_setQualificationStepsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationStepsData(data)

    def as_setQualificationDataS(self, imageSrcSmall, imageSrcBig, isFirstEnter):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationData(imageSrcSmall, imageSrcBig, isFirstEnter)

    def as_setQualificationProgressS(self, progressTextSmall, progressTextBig, isCompleted, descr):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationProgress(progressTextSmall, progressTextBig, isCompleted, descr)