# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mapbox/mapbox_entry_point_view.py
from constants import Configs
from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.gen.view_models.views.lobby.mapbox.mapbox_entry_point_view_model import MapboxEntryPointViewModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from helpers import dependency, time_utils, server_settings
from skeletons.gui.game_control import IMapboxController
from skeletons.gui.lobby_context import ILobbyContext

class MapBoxEntryPointView(ViewImpl):
    __mapboxCtrl = dependency.descriptor(IMapboxController)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, flags=ViewFlags.VIEW):
        settings = ViewSettings(R.views.lobby.mapbox.MapBoxEntryPointView())
        settings.flags = flags
        settings.model = MapboxEntryPointViewModel()
        super(MapBoxEntryPointView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(MapBoxEntryPointView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(MapBoxEntryPointView, self)._initialize(*args, **kwargs)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged
        self.__mapboxCtrl.onPrimeTimeStatusUpdated += self.__onPrimeTimeUpdated
        self.viewModel.onActionClick += self.__onClick

    def _finalize(self):
        self.viewModel.onActionClick -= self.__onClick
        self.__mapboxCtrl.onPrimeTimeStatusUpdated -= self.__onPrimeTimeUpdated
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        super(MapBoxEntryPointView, self)._finalize()

    def _onLoading(self, *args, **kwargs):
        super(MapBoxEntryPointView, self)._onLoading(*args, **kwargs)
        self.__updateViewModel()

    @server_settings.serverSettingsChangeListener(Configs.MAPBOX_CONFIG.value)
    def __onServerSettingsChanged(self, _):
        self.__updateViewModel()

    def __onPrimeTimeUpdated(self, _):
        self.__updateViewModel()

    def __updateViewModel(self):
        if not isMapboxEntryPointAvailable():
            self.destroy()
            return
        with self.viewModel.transaction() as (model):
            currServerTime = time_utils.getCurrentLocalServerTimestamp()
            model.setEndDate(self.__mapboxCtrl.getEventEndTimestamp() + time_utils.getCurrentTimestamp() - currServerTime)

    def __onClick(self):
        self.__mapboxCtrl.selectMapboxBattle()


@dependency.replace_none_kwargs(mapboxCtrl=IMapboxController)
def isMapboxEntryPointAvailable(mapboxCtrl=None):
    return mapboxCtrl.isEnabled() and (mapboxCtrl.hasPrimeTimesLeftForCurrentCycle() or mapboxCtrl.isInPrimeTime())