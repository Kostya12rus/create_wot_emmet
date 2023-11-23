# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/mapbox/pre_queue/permissions.py
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from helpers import dependency
from skeletons.gui.game_control import IMapboxController

class MapboxPermissions(PreQueuePermissions):
    __mapboxController = dependency.descriptor(IMapboxController)

    def canCreateSquad(self):
        if self.__mapboxController.isInPrimeTime():
            return super(MapboxPermissions, self).canCreateSquad()
        return False