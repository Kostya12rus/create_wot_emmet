# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_cm_handlers.py
from gui.impl.lobby.crew.widget.crew_widget_cm_handlers import CrewContextMenuHandler, CREW
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from uilogging.crew.logging_constants import CrewViewKeys
VISIBLE_OPTIONS = (
 CREW.PERSONAL_FILE,
 CREW.DISMISS,
 CREW.QUICK_TRAINING,
 CREW.SEND_TO_BARRACKS)

class CrewTankmanContextMenuHandler(CrewContextMenuHandler):
    itemsCache = dependency.descriptor(IItemsCache)

    def _generateOptions(self, ctx=None):
        options = super(CrewTankmanContextMenuHandler, self)._generateOptions(ctx)
        return [ option for option in options if option.get('id') in VISIBLE_OPTIONS ]

    def _initFlashValues(self, ctx):
        tankmanID = int(ctx.tankmanID)
        self._slotIdx = int(ctx.slotIdx)
        self._tankmanID = tankmanID
        self._vehicle = self.itemsCache.items.getVehicle(self.itemsCache.items.getTankman(tankmanID).vehicleInvID)
        self._previousViewID = None
        self._uiLogger.setParentViewKey(CrewViewKeys.BARRACKS)
        self._parentViewKey = CrewViewKeys.BARRACKS
        return