# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameMenuMeta(AbstractWindowView):

    def quitBattleClick(self):
        self._printOverrideError('quitBattleClick')

    def settingsClick(self):
        self._printOverrideError('settingsClick')

    def helpClick(self):
        self._printOverrideError('helpClick')

    def cancelClick(self):
        self._printOverrideError('cancelClick')

    def onCounterNeedUpdate(self):
        self._printOverrideError('onCounterNeedUpdate')

    def bootcampClick(self):
        self._printOverrideError('bootcampClick')

    def as_setServerSettingS(self, serverName, tooltipFullData, serverState):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerSetting(serverName, tooltipFullData, serverState)

    def as_setServerStatsS(self, stats, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)

    def as_setCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounter(counters)

    def as_removeCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_removeCounter(counters)

    def as_setMenuButtonsLabelsS(self, helpLabel, settingsLabel, cancelLabel, quitLabel, bootcampLabel, bootcampIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuButtonsLabels(helpLabel, settingsLabel, cancelLabel, quitLabel, bootcampLabel, bootcampIcon)

    def as_showQuitButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showQuitButton(value)

    def as_showBootcampButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBootcampButton(value)

    def as_showHelpButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpButton(value)