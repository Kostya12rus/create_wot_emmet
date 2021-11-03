# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/ammunition_items_group.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_setup_selector import AmmunitionSetupSelector

class AmmunitionItemsGroup(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(AmmunitionItemsGroup, self).__init__(properties=properties, commands=commands)

    @property
    def setupSelector(self):
        return self._getViewModel(0)

    def getSections(self):
        return self._getArray(1)

    def setSections(self, value):
        self._setArray(1, value)

    def getCurrentIndex(self):
        return self._getNumber(2)

    def setCurrentIndex(self, value):
        self._setNumber(2, value)

    def getGroupId(self):
        return self._getNumber(3)

    def setGroupId(self, value):
        self._setNumber(3, value)

    def getTotalCount(self):
        return self._getNumber(4)

    def setTotalCount(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(AmmunitionItemsGroup, self)._initialize()
        self._addViewModelProperty('setupSelector', AmmunitionSetupSelector())
        self._addArrayProperty('sections', Array())
        self._addNumberProperty('currentIndex', 0)
        self._addNumberProperty('groupId', 0)
        self._addNumberProperty('totalCount', 0)