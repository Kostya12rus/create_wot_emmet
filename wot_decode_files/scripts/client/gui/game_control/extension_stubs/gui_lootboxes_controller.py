# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/extension_stubs/gui_lootboxes_controller.py
from skeletons.gui.game_control import IGuiLootBoxesController
import Event

class GuiLootBoxesControllerStub(IGuiLootBoxesController):
    onStatusChange = Event.Event()
    onAvailabilityChange = Event.Event()
    onBoxesCountChange = Event.Event()
    onWelcomeScreenClosed = Event.Event()

    @property
    def boxCountToGuaranteedBonus(self):
        return 0

    @property
    def isConsumesEntitlements(self):
        return False

    def getGuaranteedBonusLimit(self, boxType):
        return 0

    def getSetting(self, setting):
        return

    def setSetting(self, setting, value):
        pass

    def getBoxInfo(self, boxType):
        return {}

    def getVehicleLevels(self, boxType):
        return set()

    def isEnabled(self):
        return False

    def isLootBoxesAvailable(self):
        return False

    def isBuyAvailable(self):
        return False

    def isFirstStorageEnter(self):
        return True

    def setStorageVisited(self):
        pass

    def getDayLimit(self):
        return 0

    def openShop(self):
        pass

    def getDayInfoStatistics(self):
        return {}

    def getExpiresAtLootBoxBuyCounter(self):
        return 0

    def getTimeLeftToResetPurchase(self):
        return 0

    def getStoreInfo(self):
        return {}

    def getBoxesIDs(self):
        return ()

    def getBoxesCount(self):
        return 0

    def getBoxesInfo(self):
        return {}

    def getBonusesOrder(self, category=None):
        return tuple()

    def getHangarOptimizer(self):
        return