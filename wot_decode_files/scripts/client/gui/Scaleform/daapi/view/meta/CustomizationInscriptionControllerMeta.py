# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationInscriptionControllerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationInscriptionControllerMeta(BaseDAAPIComponent):

    def sendChar(self, char):
        self._printOverrideError('sendChar')

    def finish(self):
        self._printOverrideError('finish')

    def removeChar(self):
        self._printOverrideError('removeChar')

    def deleteAll(self):
        self._printOverrideError('deleteAll')

    def as_showS(self, inscriptionLength):
        if self._isDAAPIInited():
            return self.flashObject.as_show(inscriptionLength)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()

    def as_invalidInscriptionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_invalidInscription(data)

    def as_showHintS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(data)