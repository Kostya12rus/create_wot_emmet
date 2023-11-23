# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PostmortemPanelMeta.py
from gui.Scaleform.daapi.view.meta.BasePostmortemPanelMeta import BasePostmortemPanelMeta

class PostmortemPanelMeta(BasePostmortemPanelMeta):

    def onDogTagKillerInPlaySound(self):
        self._printOverrideError('onDogTagKillerInPlaySound')

    def onDogTagKillerOutPlaySound(self):
        self._printOverrideError('onDogTagKillerOutPlaySound')

    def onVictimDogTagInPlaySound(self):
        self._printOverrideError('onVictimDogTagInPlaySound')

    def as_showDeadReasonS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showDeadReason()

    def as_setPlayerInfoS(self, playerInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerInfo(playerInfo)

    def as_showKillerDogTagS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showKillerDogTag(data)

    def as_showVictimDogTagS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showVictimDogTag(data)

    def as_preloadComponentsS(self, components):
        if self._isDAAPIInited():
            return self.flashObject.as_preloadComponents(components)

    def as_hideComponentsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideComponents()