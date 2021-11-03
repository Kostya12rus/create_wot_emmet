# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanSearchInfoMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanSearchInfoMeta(BaseDAAPIComponent):

    def sendRequest(self):
        self._printOverrideError('sendRequest')

    def openClanProfile(self):
        self._printOverrideError('openClanProfile')

    def requestData(self, clanId):
        self._printOverrideError('requestData')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStateDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStateData(data)

    def as_setEmblemS(self, emblem):
        if self._isDAAPIInited():
            return self.flashObject.as_setEmblem(emblem)

    def as_setWaitingVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingVisible(visible)

    def as_setDummyS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)

    def as_setDummyVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)