# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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