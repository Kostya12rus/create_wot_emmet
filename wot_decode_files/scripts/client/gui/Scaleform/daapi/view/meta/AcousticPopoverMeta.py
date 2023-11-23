# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AcousticPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class AcousticPopoverMeta(SmartPopOverView):

    def onActionStart(self, actionID):
        self._printOverrideError('onActionStart')

    def onSpeakerClick(self, speakerID):
        self._printOverrideError('onSpeakerClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_onItemPlayS(self, itemsID):
        if self._isDAAPIInited():
            return self.flashObject.as_onItemPlay(itemsID)

    def as_onItemSelectS(self, itemsID):
        if self._isDAAPIInited():
            return self.flashObject.as_onItemSelect(itemsID)

    def as_setEnableS(self, isEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnable(isEnable)

    def as_updateBtnEnabledS(self, btnId, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBtnEnabled(btnId, isEnabled)