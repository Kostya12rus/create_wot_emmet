# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_header_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.crew_header_tooltip_view_model import CrewHeaderTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
_MINUTES_IN_HOUR = 60

class CrewHeaderTooltipView(ViewImpl):
    __slots__ = ('_serverSettings', )
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(layoutID=R.views.lobby.crew.CrewHeaderTooltipView(), model=CrewHeaderTooltipViewModel())
        settings.args = args
        settings.kwargs = kwargs
        self._serverSettings = self._lobbyContext.getServerSettings()
        super(CrewHeaderTooltipView, self).__init__(settings, *args, **kwargs)

    @property
    def viewModel(self):
        return super(CrewHeaderTooltipView, self).getViewModel()

    def _onLoading(self, isActive, warningStr):
        with self.viewModel.transaction() as (tx):
            tx.setIsActive(isActive)
            tx.setBonusXpPerHour(self._serverSettings.getRenewableSubCrewXPPerMinute() * _MINUTES_IN_HOUR)
            tx.setWarning(warningStr)