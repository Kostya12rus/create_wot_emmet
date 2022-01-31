# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/NewYearCelebrityEntryObject.py
import BigWorld
from NewYearBaseEntryObject import NewYearBaseEntryObject
from gui.impl.new_year.navigation import NewYearNavigation
from gui.impl.new_year.sounds import NewYearSoundsManager, NewYearSoundEvents
from new_year.ny_constants import AnchorNames
from helpers import dependency
from skeletons.new_year import ICelebritySceneController
from uilogging.ny.mixins import SelectableObjectLoggerMixin

class NewYearCelebrityEntryObject(NewYearBaseEntryObject, SelectableObjectLoggerMixin):
    _celebrityController = dependency.descriptor(ICelebritySceneController)

    def __init__(self):
        super(NewYearCelebrityEntryObject, self).__init__()
        self.__alphaFadeFashion = None
        return

    def onEnterWorld(self, prereqs):
        super(NewYearCelebrityEntryObject, self).onEnterWorld(prereqs)
        self.__alphaFadeFashion = BigWorld.WGAlphaFadeFashion()
        self.__alphaFadeFashion.minAlpha = self.minAlpha
        self.__alphaFadeFashion.maxAlphaDist = self.maxAlphaDistance * self.maxAlphaDistance
        self.model.fashion = self.__alphaFadeFashion
        self._celebrityController.addCelebrityEntryEntity(self)

    def onLeaveWorld(self):
        self._celebrityController.removeCelebrityEntryEntity()
        super(NewYearCelebrityEntryObject, self).onLeaveWorld()

    def onMouseClick(self):
        super(NewYearCelebrityEntryObject, self).onMouseClick()
        NewYearSoundsManager.playEvent(NewYearSoundEvents.ENTER_CUSTOME)
        self.logClick(AnchorNames.CELEBRITY)
        NewYearNavigation.switchByAnchorName(AnchorNames.CELEBRITY)