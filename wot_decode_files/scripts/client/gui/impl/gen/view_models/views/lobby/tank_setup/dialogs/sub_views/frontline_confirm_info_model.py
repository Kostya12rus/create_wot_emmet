# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/sub_views/frontline_confirm_info_model.py
from frameworks.wulf import ViewModel

class FrontlineConfirmInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FrontlineConfirmInfoModel, self).__init__(properties=properties, commands=commands)

    def getBonus(self):
        return self._getNumber(0)

    def setBonus(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(FrontlineConfirmInfoModel, self)._initialize()
        self._addNumberProperty('bonus', 0)