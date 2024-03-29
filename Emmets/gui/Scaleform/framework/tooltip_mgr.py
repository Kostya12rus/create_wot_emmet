# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/tooltip_mgr.py
import inspect, itertools, logging, BigWorld, Keys
from collections import namedtuple
from Event import SafeEvent, EventManager
from gui import InputHandler
from gui.Scaleform.framework.entities.abstract.ToolTipMgrMeta import ToolTipMgrMeta
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared import events
from gui.shared.tooltips import builders
from helpers import dependency, uniprof
from ids_generators import SequenceIDGenerator
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.impl import IGuiLoader
from soft_exception import SoftException
ToolTipInfo = namedtuple('ToolTipInfo', ('id', 'region', 'name'))
_logger = logging.getLogger(__name__)
_id_generator = SequenceIDGenerator()
LIVE_REGION_COLOR = 9611473
LOADING_REGION_COLOR = 12757201
_TOOLTIP_VARIANT_TYPED = 'typed'
_TOOLTIP_VARIANT_COMPLEX = 'complex'
_TOOLTIP_VARIANT_WULF = 'wulf'

class ToolTip(ToolTipMgrMeta):
    appLoader = dependency.descriptor(IAppLoader)
    gui = dependency.descriptor(IGuiLoader)

    def __init__(self, settings, advComplexSettings, *noTooltipSpaceIDs):
        super(ToolTip, self).__init__()
        self._areTooltipsDisabled = False
        self._isAllowedTypedTooltip = True
        self._noTooltipSpaceIDs = noTooltipSpaceIDs
        self._complex = builders.ComplexBuilder(TOOLTIPS_CONSTANTS.DEFAULT, TOOLTIPS_CONSTANTS.COMPLEX_UI, advComplexSettings)
        self._builders = builders.LazyBuildersCollection(settings)
        self._builders.addBuilder(builders.SimpleBuilder(TOOLTIPS_CONSTANTS.DEFAULT, TOOLTIPS_CONSTANTS.COMPLEX_UI))
        self._dynamic = {}
        self.__fastRedraw = False
        self.__isAdvancedKeyPressed = False
        self.__tooltipVariant = None
        self.__tooltipID = None
        self.__args = None
        self.__stateType = None
        self.__tooltipInfos = []
        self.__tooltipWindowId = 0
        self.__em = EventManager()
        self.onShow = SafeEvent(self.__em)
        self.onHide = SafeEvent(self.__em)
        return

    def show(self, data, linkage):
        self.as_showS(data, linkage, self.__fastRedraw)

    def hide(self):
        self.as_hideS()

    def handleKeyEvent(self, event):
        if not self.isReadyToHandleKey(event):
            return
        tooltipType = self.__tooltipID
        args = self.__args
        isSupportAdvanced = self.isSupportAdvanced(tooltipType, *args)
        if isSupportAdvanced:
            self.__fastRedraw = True
            if self.__tooltipVariant == _TOOLTIP_VARIANT_COMPLEX:
                self.onCreateComplexTooltip(tooltipType, self.__stateType)
            else:
                if self.__tooltipVariant == _TOOLTIP_VARIANT_TYPED:
                    self.onCreateTypedTooltip(tooltipType, args, self.__stateType)
                elif self.__tooltipVariant == _TOOLTIP_VARIANT_WULF:
                    self.onCreateWulfTooltip(tooltipType, args, *self.__stateType)

    def isReadyToHandleKey(self, event):
        altPressed = event.key == Keys.KEY_LALT or event.key == Keys.KEY_RALT
        self.__isAdvancedKeyPressed = event.isKeyDown() and altPressed
        return self.__tooltipID is not None and altPressed

    def getTypedTooltipDefaultBuildArgs(self, tooltipType):
        builder = self._builders.getBuilder(tooltipType)
        if builder is None:
            raise SoftException('Builder for tooltip: type "%s" is not found', tooltipType)
        provider = builder.provider
        if provider is None:
            raise SoftException('"%s" does not have any provider', builder.__name__)
        spec = inspect.getargspec(provider.context.buildItem)
        return tuple(reversed([ (argName, defaultValue) for argName, defaultValue in itertools.izip_longest(reversed(spec.args), reversed(spec.defaults or [])) if argName != 'self'
                              ]))

    def onCreateTypedTooltip(self, tooltipType, args, stateType):
        if self._areTooltipsDisabled:
            return
        else:
            if not self._isAllowedTypedTooltip:
                return
            id = _id_generator.next()
            region = ('Typed tooltip {} {}').format(tooltipType, id)
            name = ('tooltip {}').format(tooltipType)
            info = ToolTipInfo(id, region, name)
            self.__tooltipInfos.append(info)
            uniprof.enterToRegion(region, LIVE_REGION_COLOR)
            BigWorld.notify(BigWorld.EventType.VIEW_CREATED, name, id, name)
            builder = self._builders.getBuilder(tooltipType)
            if builder is not None:
                region = ('Loading {} {}').format(tooltipType, id)
                uniprof.enterToRegion(region, LOADING_REGION_COLOR)
                BigWorld.notify(BigWorld.EventType.LOADING_VIEW, name, id, name)
                try:
                    data = builder.build(self, stateType, self.__isAdvancedKeyPressed, *args)
                except:
                    BigWorld.notify(BigWorld.EventType.LOAD_FAILED, name, id, name)
                    uniprof.exitFromRegion(region)
                    raise

                BigWorld.notify(BigWorld.EventType.VIEW_LOADED, name, id, name)
                uniprof.exitFromRegion(region)
            else:
                _logger.warning('Tooltip can not be displayed: type "%s" is not found', tooltipType)
                return
            self.__cacheTooltipData(_TOOLTIP_VARIANT_TYPED, tooltipType, args, stateType)
            self.onShow(tooltipType, args, self.__isAdvancedKeyPressed)
            if data is not None and data.isDynamic():
                data.changeVisibility(True)
                if tooltipType not in self._dynamic:
                    self._dynamic[tooltipType] = data
            return

    def onCreateWulfTooltip(self, tooltipType, args, x, y):
        if not self._isAllowedTypedTooltip:
            return
        else:
            builder = self._builders.getBuilder(tooltipType)
            if builder is not None:
                data = builder.build(self, None, self.__isAdvancedKeyPressed, *args)
            else:
                _logger.warning('Tooltip can not be displayed: type "%s" is not found', tooltipType)
                return
            window = data.getDisplayableData(*args)
            window.load()
            window.move(x, y)
            self.__tooltipWindowId = window.uniqueID
            self.__cacheTooltipData(_TOOLTIP_VARIANT_WULF, tooltipType, args, (x, y))
            self.onShow(tooltipType, args, self.__isAdvancedKeyPressed)
            return

    def onCreateComplexTooltip(self, tooltipID, stateType):
        if self._areTooltipsDisabled:
            return
        else:
            id = _id_generator.next()
            region = ('Complex tooltip {} {}').format(tooltipID, id)
            info = ToolTipInfo(id, region, None)
            self.__tooltipInfos.append(info)
            uniprof.enterToRegion(region, LIVE_REGION_COLOR)
            self._complex.build(self, stateType, self.__isAdvancedKeyPressed, tooltipID)
            self.__cacheTooltipData(_TOOLTIP_VARIANT_COMPLEX, tooltipID, tuple(), stateType)
            self.onShow(tooltipID, None, self.__isAdvancedKeyPressed)
            return

    def onHideTooltip(self, tooltipId):
        if not self._areTooltipsDisabled and tooltipId in self._dynamic:
            self._dynamic[tooltipId].changeVisibility(False)
        hideTooltipId = tooltipId or self.__tooltipID or ''
        self.__tooltipID = None
        self.__fastRedraw = False
        self.__destroyTooltipWindow()
        if self.__tooltipInfos:
            info = self.__tooltipInfos.pop(0)
            if info.name is not None:
                BigWorld.notify(BigWorld.EventType.VIEW_DESTROYED, info.name, info.id, info.name)
            uniprof.exitFromRegion(info.region)
        self.onHide(hideTooltipId)
        return

    def _populate(self):
        super(ToolTip, self)._populate()
        self.appLoader.onGUISpaceEntered += self.__onGUISpaceEntered
        self.addListener(events.AppLifeCycleEvent.CREATING, self.__onAppCreating)
        InputHandler.g_instance.onKeyDown += self.handleKeyEvent
        InputHandler.g_instance.onKeyUp += self.handleKeyEvent

    def _dispose(self):
        self._builders.clear()
        self.appLoader.onGUISpaceEntered -= self.__onGUISpaceEntered
        self.removeListener(events.AppLifeCycleEvent.CREATING, self.__onAppCreating)
        while self._dynamic:
            _, data = self._dynamic.popitem()
            data.stopUpdates()

        InputHandler.g_instance.onKeyDown -= self.handleKeyEvent
        InputHandler.g_instance.onKeyUp -= self.handleKeyEvent
        self.__destroyTooltipWindow()
        self.__em.clear()
        super(ToolTip, self)._dispose()

    def __onGUISpaceEntered(self, spaceID):
        self._isAllowedTypedTooltip = spaceID not in self._noTooltipSpaceIDs

    def __onAppCreating(self, appNS):
        if self.app.appNS != appNS:
            self._areTooltipsDisabled = True

    def isSupportAdvanced(self, tooltipType, *args):
        isComplex = self.__tooltipVariant == _TOOLTIP_VARIANT_COMPLEX
        builder = self._complex if isComplex else self._builders.getBuilder(tooltipType)
        if builder is None:
            return False
        else:
            return builder.supportAdvanced(tooltipType, *args)

    def __cacheTooltipData(self, tooltipType, tooltipID, args, stateType):
        self.__tooltipVariant = tooltipType
        self.__tooltipID = tooltipID
        self.__args = args
        self.__stateType = stateType

    def __destroyTooltipWindow(self):
        if self.__tooltipWindowId:
            window = self.gui.windowsManager.getWindow(self.__tooltipWindowId)
            if window is not None:
                window.destroy()
            self.__tooltipWindowId = 0
        return