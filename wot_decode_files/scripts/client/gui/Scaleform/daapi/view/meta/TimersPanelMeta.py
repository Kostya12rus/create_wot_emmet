# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TimersPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TimersPanelMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_showS(self, timerTypeID, timerViewTypeID, isBubble):
        if self._isDAAPIInited():
            return self.flashObject.as_show(timerTypeID, timerViewTypeID, isBubble)

    def as_hideS(self, timerTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(timerTypeID)

    def as_setVerticalOffsetS(self, offsetY):
        if self._isDAAPIInited():
            return self.flashObject.as_setVerticalOffset(offsetY)

    def as_setTimeInSecondsS(self, timerTypeID, totalSeconds, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeInSeconds(timerTypeID, totalSeconds, currentTime)

    def as_setTimeSnapshotS(self, timerTypeID, totalSeconds, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeSnapshot(timerTypeID, totalSeconds, timeLeft)

    def as_setSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeed(speed)

    def as_turnOnStackViewS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_turnOnStackView(value)

    def as_setTimerTextS(self, timerID, title, description=''):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerText(timerID, title, description)

    def as_showSecondaryTimerS(self, secTimerID, totalSeconds, currentTime, secondInRow):
        if self._isDAAPIInited():
            return self.flashObject.as_showSecondaryTimer(secTimerID, totalSeconds, currentTime, secondInRow)

    def as_hideSecondaryTimerS(self, secTimerID):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSecondaryTimer(secTimerID)

    def as_setSecondaryTimeSnapshotS(self, secTimerID, totalSeconds, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryTimeSnapshot(secTimerID, totalSeconds, currentTime)

    def as_setSecondaryTimerTextS(self, secTimerID, title, description=''):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryTimerText(secTimerID, title, description)