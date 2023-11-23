# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractTweenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class AbstractTweenMeta(BaseDAAPIModule):

    def initialiaze(self, props):
        self._printOverrideError('initialiaze')

    def creatTweenPY(self, tween):
        self._printOverrideError('creatTweenPY')

    def getPaused(self):
        self._printOverrideError('getPaused')

    def setPaused(self, paused):
        self._printOverrideError('setPaused')

    def getLoop(self):
        self._printOverrideError('getLoop')

    def setLoop(self, loop):
        self._printOverrideError('setLoop')

    def getDuration(self):
        self._printOverrideError('getDuration')

    def setDuration(self, duration):
        self._printOverrideError('setDuration')

    def getPosition(self):
        self._printOverrideError('getPosition')

    def setPosition(self, position):
        self._printOverrideError('setPosition')

    def getDelay(self):
        self._printOverrideError('getDelay')

    def setDelay(self, delay):
        self._printOverrideError('setDelay')

    def resetAnim(self):
        self._printOverrideError('resetAnim')

    def getTweenIdx(self):
        self._printOverrideError('getTweenIdx')

    def getIsComplete(self):
        self._printOverrideError('getIsComplete')

    def postponedCheckState(self):
        self._printOverrideError('postponedCheckState')

    def getTargetDisplayObjectS(self):
        if self._isDAAPIInited():
            return self.flashObject.getTargetDisplayObject()

    def onAnimCompleteS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimComplete()

    def onAnimStartS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimStart()