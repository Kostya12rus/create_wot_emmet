# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ClientSelectableRankedObject.py
from ClientSelectableObject import ClientSelectableObject
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class ClientSelectableRankedObject(ClientSelectableObject):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def onEnterWorld(self, prereqs):
        super(ClientSelectableRankedObject, self).onEnterWorld(prereqs)
        self.__rankedController.onGameModeStatusUpdated += self.__onGameModeStatusUpdate
        self.__onGameModeStatusUpdate()

    def onLeaveWorld(self):
        self.__rankedController.onGameModeStatusUpdated -= self.__onGameModeStatusUpdate
        super(ClientSelectableRankedObject, self).onLeaveWorld()

    def onMouseClick(self):
        super(ClientSelectableRankedObject, self).onMouseClick()
        self.__rankedController.doActionOnEntryPointClick()

    def __onGameModeStatusUpdate(self, *_):
        isEnabled = self.__rankedController.isEnabled()
        hasCurSeason = self.__rankedController.getCurrentSeason() is not None
        hasPrevSeason = self.__rankedController.getPreviousSeason() is not None
        if isEnabled and not hasCurSeason and not hasPrevSeason:
            self.setEnable(False)
        else:
            self.setEnable(True)
        return