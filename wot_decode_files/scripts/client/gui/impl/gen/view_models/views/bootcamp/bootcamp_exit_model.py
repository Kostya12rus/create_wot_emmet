# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/bootcamp/bootcamp_exit_model.py
from gui.impl.gen.view_models.views.bootcamp.bootcamp_progress_model import BootcampProgressModel

class BootcampExitModel(BootcampProgressModel):
    __slots__ = ('onLeaveBootcamp', )

    def __init__(self, properties=7, commands=1):
        super(BootcampExitModel, self).__init__(properties=properties, commands=commands)

    def getIsInBattle(self):
        return self._getBool(4)

    def setIsInBattle(self, value):
        self._setBool(4, value)

    def getIsNeedAwarding(self):
        return self._getBool(5)

    def setIsNeedAwarding(self, value):
        self._setBool(5, value)

    def getIsReferral(self):
        return self._getBool(6)

    def setIsReferral(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(BootcampExitModel, self)._initialize()
        self._addBoolProperty('isInBattle', False)
        self._addBoolProperty('isNeedAwarding', False)
        self._addBoolProperty('isReferral', False)
        self.onLeaveBootcamp = self._addCommand('onLeaveBootcamp')