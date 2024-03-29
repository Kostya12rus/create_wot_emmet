# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/daily_quests_injector_view.py
from gui.Scaleform.daapi.view.meta.MissionsPremiumViewMeta import MissionsPremiumViewMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.missions.daily_quests_view import DailyQuestsView

class DailyQuestsInjectorView(InjectComponentAdaptor, MissionsPremiumViewMeta):
    __slots__ = ()

    def setDefaultTab(self, tabIdx):
        if self._injectView is not None:
            self._injectView.setDefaultTab(tabIdx)
        return

    def changeTab(self, tabIdx):
        if self._injectView is not None:
            self._injectView.changeTab(tabIdx)
        return

    def markVisited(self):
        if self._injectView is not None:
            self._injectView.markVisited()
            self._injectView.resetInfoPageVisibility()
        return

    def setProxy(self, proxy):
        if self._injectView is not None:
            self._injectView.setProxy(proxy)
        return

    def _makeInjectView(self):
        return DailyQuestsView()