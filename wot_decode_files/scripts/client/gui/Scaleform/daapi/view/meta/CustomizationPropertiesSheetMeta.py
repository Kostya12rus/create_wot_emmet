# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationPropertiesSheetMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationPropertiesSheetMeta(BaseDAAPIComponent):

    def onActionBtnClick(self, actionType, actionData):
        self._printOverrideError('onActionBtnClick')

    def elementControlsHide(self):
        self._printOverrideError('elementControlsHide')

    def onClose(self):
        self._printOverrideError('onClose')

    def registerInscriptionController(self, inscriptionController, inputLines):
        self._printOverrideError('registerInscriptionController')

    def as_setDataAndShowS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDataAndShow(data)

    def as_setArrowsStatesS(self, left, right):
        if self._isDAAPIInited():
            return self.flashObject.as_setArrowsStates(left, right)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()