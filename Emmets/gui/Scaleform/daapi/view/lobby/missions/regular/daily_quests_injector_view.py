# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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