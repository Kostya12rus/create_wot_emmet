# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/NewYearHeroTank.py
from HeroTank import HeroTank
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates
from gui.impl.new_year.navigation import NewYearNavigation

class NewYearHeroTank(HeroTank):

    def onSelect(self):
        self.setState(CameraMovementStates.MOVING_TO_OBJECT)
        NewYearNavigation.switchToHeroTank()
        self.setState(CameraMovementStates.ON_OBJECT)

    def onDeselect(self, newSelectedObject):
        self.setState(CameraMovementStates.FROM_OBJECT)
        if not newSelectedObject:
            return
        newSelectedObject.setState(CameraMovementStates.MOVING_TO_OBJECT)
        NewYearNavigation.switchFromHeroTank()
        newSelectedObject.setState(CameraMovementStates.ON_OBJECT)