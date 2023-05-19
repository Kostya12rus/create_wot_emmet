# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionOperationsMeta.py
from gui.Scaleform.framework.entities.View import View

class PersonalMissionOperationsMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def onOperationClick(self, pmType, operationID):
        self._printOverrideError('onOperationClick')

    def showInfo(self):
        self._printOverrideError('showInfo')

    def as_setOperationsS(self, operations):
        if self._isDAAPIInited():
            return self.flashObject.as_setOperations(operations)

    def as_setTitleS(self, titleVO):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(titleVO)