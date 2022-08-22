# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/wot_anniversary/dragon_boat_finish_view_model.py
from frameworks.wulf import ViewModel

class DragonBoatFinishViewModel(ViewModel):
    __slots__ = ('onClose', 'onPickNewTeamBtnClick')

    def __init__(self, properties=1, commands=2):
        super(DragonBoatFinishViewModel, self).__init__(properties=properties, commands=commands)

    def getTeam(self):
        return self._getNumber(0)

    def setTeam(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(DragonBoatFinishViewModel, self)._initialize()
        self._addNumberProperty('team', -1)
        self.onClose = self._addCommand('onClose')
        self.onPickNewTeamBtnClick = self._addCommand('onPickNewTeamBtnClick')