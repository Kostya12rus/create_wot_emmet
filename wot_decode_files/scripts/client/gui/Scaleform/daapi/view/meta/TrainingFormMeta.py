# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingFormMeta.py
from gui.Scaleform.framework.entities.View import View

class TrainingFormMeta(View):

    def joinTrainingRequest(self, id):
        self._printOverrideError('joinTrainingRequest')

    def createTrainingRequest(self):
        self._printOverrideError('createTrainingRequest')

    def onEscape(self):
        self._printOverrideError('onEscape')

    def onLeave(self):
        self._printOverrideError('onLeave')

    def as_setInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(data)

    def as_setListS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setList(data)