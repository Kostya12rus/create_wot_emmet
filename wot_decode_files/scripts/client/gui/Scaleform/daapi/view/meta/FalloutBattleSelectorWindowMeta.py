# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBattleSelectorWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FalloutBattleSelectorWindowMeta(AbstractWindowView):

    def onDominationBtnClick(self):
        self._printOverrideError('onDominationBtnClick')

    def onMultiteamBtnClick(self):
        self._printOverrideError('onMultiteamBtnClick')

    def onSelectCheckBoxAutoSquad(self, isSelected):
        self._printOverrideError('onSelectCheckBoxAutoSquad')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setBtnStatesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnStates(data)

    def as_setTooltipsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTooltips(data)