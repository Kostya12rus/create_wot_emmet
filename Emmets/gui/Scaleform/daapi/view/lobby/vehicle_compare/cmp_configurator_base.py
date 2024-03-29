# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_base.py
from gui.Scaleform.daapi.view.meta.VehicleCompareConfiguratorBaseViewMeta import VehicleCompareConfiguratorBaseViewMeta

class VehicleCompareConfiguratorBaseView(VehicleCompareConfiguratorBaseViewMeta):

    def __init__(self):
        super(VehicleCompareConfiguratorBaseView, self).__init__()
        self._container = None
        self.__isInited = False
        return

    def onShow(self):
        pass

    def onCamouflageUpdated(self):
        pass

    def onShellsUpdated(self, updateShells=False, selectedIndex=-1):
        pass

    def onOptDeviceUpdated(self):
        pass

    def onEquipmentUpdated(self):
        pass

    def onBattleBoosterUpdated(self):
        pass

    def onModulesUpdated(self):
        pass

    def onCrewSkillUpdated(self):
        pass

    def onCrewLevelUpdated(self, newLvl):
        pass

    def onPostProgressionUpdated(self):
        pass

    def onResetToDefault(self):
        pass

    def onBasketParametersChanged(self, basketVehData):
        pass

    def setContainer(self, container):
        self._container = container
        self.__tryToInit()

    def _init(self):
        pass

    def _populate(self):
        super(VehicleCompareConfiguratorBaseView, self)._populate()
        self.__tryToInit()

    def _dispose(self):
        self._container = None
        super(VehicleCompareConfiguratorBaseView, self)._dispose()
        return

    def __tryToInit(self):
        if self.isCreated() and self._container is not None and not self.__isInited:
            self.__isInited = True
            self._init()
        return