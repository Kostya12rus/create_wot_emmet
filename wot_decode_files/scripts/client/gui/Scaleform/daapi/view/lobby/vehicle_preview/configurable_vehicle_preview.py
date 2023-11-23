# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/configurable_vehicle_preview.py
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from shared_utils import CONST_CONTAINER

class OptionalBlocks(CONST_CONTAINER):
    BUYING_PANEL = 'buyingPanel'
    CLOSE_BUTTON = 'closeBtn'
    ALL = (BUYING_PANEL, CLOSE_BUTTON)


class ConfigurableVehiclePreview(VehiclePreview):

    def __init__(self, ctx):
        super(ConfigurableVehiclePreview, self).__init__(ctx)
        self.__hiddenBlocks = ctx.get('hiddenBlocks')
        self.__showCloseBtn = OptionalBlocks.CLOSE_BUTTON not in self.__hiddenBlocks

    def setBottomPanel(self):
        if OptionalBlocks.BUYING_PANEL in self.__hiddenBlocks:
            self.as_setBottomPanelS('')
        else:
            super(ConfigurableVehiclePreview, self).setBottomPanel()

    def _getData(self):
        result = super(ConfigurableVehiclePreview, self)._getData()
        result.update({'showCloseBtn': self.__showCloseBtn})
        return result

    def _getExitEvent(self):
        exitEvent = super(ConfigurableVehiclePreview, self)._getExitEvent()
        exitEvent.ctx.update({'hiddenBlocks': self.__hiddenBlocks})
        return exitEvent