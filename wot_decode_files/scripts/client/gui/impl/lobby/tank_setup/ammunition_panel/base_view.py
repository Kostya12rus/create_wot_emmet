# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/base_view.py
import logging
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from Event import Event
from frameworks.wulf import ViewFlags, ViewSettings, ViewStatus
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow
from gui.impl.backport.backport_context_menu import BackportContextMenuWindow
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel
from gui.impl.lobby.halloween.tooltips.nitro_tooltip import NitroTooltip
from gui.impl.lobby.tank_setup.ammunition_panel.hangar import HangarAmmunitionPanel
from gui.impl.lobby.tank_setup.backports.context_menu import getHangarContextMenuData
from gui.impl.lobby.tank_setup.backports.tooltips import getSlotTooltipData, getSlotSpecTooltipData
from gui.impl.lobby.tank_setup.tank_setup_helper import setLastSlotAction, clearLastSlotAction
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_event_controller import IGameEventController
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
_logger = logging.getLogger(__name__)

class BaseAmmunitionPanelView(ViewImpl):
    _itemsCache = dependency.descriptor(IItemsCache)
    _hangarSpace = dependency.descriptor(IHangarSpace)
    _gameEventController = dependency.descriptor(IGameEventController)
    __slots__ = ('_ammunitionPanel', 'onSizeChanged', 'onPanelSectionSelected', 'onPanelSectionResized',
                 'onVehicleChanged', 'onEscKeyDown')

    def __init__(self, layoutId=R.views.lobby.tanksetup.AmmunitionPanel(), flags=ViewFlags.VIEW):
        settings = ViewSettings(layoutId)
        settings.flags = flags
        settings.model = AmmunitionPanelViewModel()
        super(BaseAmmunitionPanelView, self).__init__(settings)
        self._ammunitionPanel = None
        self.onSizeChanged = Event()
        self.onPanelSectionSelected = Event()
        self.onPanelSectionResized = Event()
        self.onVehicleChanged = Event()
        self.onEscKeyDown = Event()
        return

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            if self._hangarSpace.spaceLoading():
                _logger.warning('Failed to get slotData. HangarSpace is currently loading.')
                return
            tooltipData = self._createToolTipData(event)
            if tooltipData is not None:
                window = BackportTooltipWindow(tooltipData, self.getParentWindow())
                window.load()
                return window
        return super(BaseAmmunitionPanelView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.halloween.tooltips.NitroTooltip():
            return NitroTooltip()

    def createContextMenu(self, event):
        if event.contentID == R.views.common.BackportContextMenu():
            contextMenuData = getHangarContextMenuData(event, self.uniqueID)
            if contextMenuData is not None:
                window = BackportContextMenuWindow(contextMenuData, self.getParentWindow())
                window.load()
                return window
        return super(BaseAmmunitionPanelView, self).createContextMenu(event)

    def setHangarSwitchAnimState(self, isComplete):
        self.viewModel.setIsReady(True)

    def setPrbSwitching(self, value):
        self.viewModel.setIsDisabled(value)

    @property
    def isEvent(self):
        currentVehicle = g_currentVehicle.item or g_currentPreviewVehicle.item
        return currentVehicle is not None and currentVehicle.isOnlyForEventBattles

    @property
    def viewModel(self):
        return super(BaseAmmunitionPanelView, self).getViewModel()

    @property
    def vehItem(self):
        return g_currentVehicle.item

    def setLastSlotAction(self, *args, **kwargs):
        setLastSlotAction(self.viewModel, self.vehItem, *args, **kwargs)

    def update(self, fullUpdate=True):
        if fullUpdate:
            clearLastSlotAction(self.viewModel)
        self.viewModel.setIsEvent(self.isEvent)
        self.viewModel.setIsMaintenanceEnabled(not g_currentVehicle.isLocked())
        self.viewModel.setIsDisabled(self._getIsDisabled())
        self._ammunitionPanel.update(self.vehItem, fullUpdate=fullUpdate)

    def destroy(self):
        self.onSizeChanged.clear()
        self.onPanelSectionSelected.clear()
        self.onPanelSectionResized.clear()
        super(BaseAmmunitionPanelView, self).destroy()

    def _createToolTipData(self, event, tooltipsMap=None):
        tooltipId = event.getArgument('tooltip')
        if tooltipId == TOOLTIPS_CONSTANTS.HANGAR_SLOT_SPEC:
            tooltipData = getSlotSpecTooltipData(event, tooltipId)
        else:
            tooltipData = getSlotTooltipData(event, g_currentVehicle.item, self.viewModel.ammunitionPanel.getSelectedSlot(), tooltipsMap=tooltipsMap)
        return tooltipData

    def _onLoading(self, *args, **kwargs):
        super(BaseAmmunitionPanelView, self)._onLoading(*args, **kwargs)
        self._ammunitionPanel = self._createAmmunitionPanel()
        self._ammunitionPanel.onLoading()

    def _onLoaded(self, *args, **kwargs):
        super(BaseAmmunitionPanelView, self)._onLoaded(*args, **kwargs)
        self.viewModel.setIsReady(True)

    def _initialize(self, *args, **kwargs):
        super(BaseAmmunitionPanelView, self)._initialize()
        self._addListeners()
        self._ammunitionPanel.initialize()
        self.update(fullUpdate=False)

    def _finalize(self):
        self._removeListeners()
        if self._ammunitionPanel:
            self._ammunitionPanel.finalize()
        super(BaseAmmunitionPanelView, self)._finalize()

    def _createAmmunitionPanel(self):
        return HangarAmmunitionPanel(self.viewModel.ammunitionPanel, self.vehItem)

    def _addListeners(self):
        self.viewModel.onViewSizeInitialized += self.__onViewSizeInitialized
        self.viewModel.ammunitionPanel.onSectionSelect += self._onPanelSectionSelected
        self.viewModel.ammunitionPanel.onSectionResized += self._onPanelSectionResized
        g_currentVehicle.onChangeStarted += self.__onVehicleChangeStarted
        g_currentVehicle.onChanged += self._currentVehicleChanged
        self._itemsCache.onSyncCompleted += self.__itemCacheChanged

    def _removeListeners(self):
        self.viewModel.onViewSizeInitialized -= self.__onViewSizeInitialized
        self.viewModel.ammunitionPanel.onSectionSelect -= self._onPanelSectionSelected
        self.viewModel.ammunitionPanel.onSectionResized -= self._onPanelSectionResized
        g_currentVehicle.onChangeStarted -= self.__onVehicleChangeStarted
        g_currentVehicle.onChanged -= self._currentVehicleChanged
        self._itemsCache.onSyncCompleted -= self.__itemCacheChanged

    def _onPanelSectionSelected(self, args):
        if not self._getIsDisabled():
            clearLastSlotAction(self.viewModel)
            self.onPanelSectionSelected(**args)

    def _onPanelSectionResized(self, kwargs):
        self.onPanelSectionResized(**kwargs)

    def _currentVehicleChanged(self):
        self.update()
        self.viewModel.setIsReady(self._getIsReady())

    def __onVehicleChangeStarted(self):
        self.viewModel.setIsReady(False)
        self.viewModel.setIsMaintenanceEnabled(False)
        self.viewModel.setIsDisabled(True)
        self.onVehicleChanged()

    def __itemCacheChanged(self, *_):
        self.update(fullUpdate=False)

    def _getIsDisabled(self):
        return not g_currentVehicle.isInHangar() or g_currentVehicle.isLocked() or g_currentVehicle.isBroken()

    def _getIsReady(self):
        return self.viewStatus == ViewStatus.LOADED

    def __onViewSizeInitialized(self, args=None):
        self.onSizeChanged(args.get('width', 0), args.get('height', 0), args.get('offsetY', 0))