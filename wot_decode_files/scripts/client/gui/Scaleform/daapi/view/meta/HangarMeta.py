# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/HangarMeta.py
from gui.Scaleform.framework.entities.View import View

class HangarMeta(View):

    def onEscape(self):
        self._printOverrideError('onEscape')

    def showHelpLayout(self):
        self._printOverrideError('showHelpLayout')

    def closeHelpLayout(self):
        self._printOverrideError('closeHelpLayout')

    def hideTeaser(self):
        self._printOverrideError('hideTeaser')

    def onTeaserClick(self):
        self._printOverrideError('onTeaserClick')

    def as_setCrewEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewEnabled(value)

    def as_setCarouselEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselEnabled(value)

    def as_setupAmmunitionPanelS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setupAmmunitionPanel(data)

    def as_setControlsVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsVisible(value)

    def as_setComp7ModifiersVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setComp7ModifiersVisible(value)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_showHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpLayout()

    def as_closeHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeHelpLayout()

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)

    def as_show3DSceneTooltipS(self, id, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show3DSceneTooltip(id, args)

    def as_hide3DSceneTooltipS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide3DSceneTooltip()

    def as_setCarouselS(self, linkage, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarousel(linkage, alias)

    def as_setAlertMessageBlockVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlertMessageBlockVisible(isVisible)

    def as_showTeaserS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showTeaser(data)

    def as_setTeaserTimerS(self, timeLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeaserTimer(timeLabel)

    def as_hideTeaserTimerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideTeaserTimer()

    def as_setNotificationEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setNotificationEnabled(value)

    def as_createDQWidgetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createDQWidget()

    def as_destroyDQWidgetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_destroyDQWidget()

    def as_showSwitchToAmmunitionS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showSwitchToAmmunition()

    def as_toggleBattleRoyaleS(self, isBattleRoyale):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleBattleRoyale(isBattleRoyale)

    def as_toggleCnSubscriptionS(self, isCnSubscription):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleCnSubscription(isCnSubscription)

    def as_setDQWidgetLayoutS(self, lyout):
        if self._isDAAPIInited():
            return self.flashObject.as_setDQWidgetLayout(lyout)

    def as_updateCarouselEventEntryStateS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCarouselEventEntryState(isVisible)