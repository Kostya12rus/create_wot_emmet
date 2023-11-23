# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/sub_views/frontline_confirm_icons_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class FrontlineConfirmIconsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FrontlineConfirmIconsModel, self).__init__(properties=properties, commands=commands)

    def getIcons(self):
        return self._getArray(0)

    def setIcons(self, value):
        self._setArray(0, value)

    @staticmethod
    def getIconsType():
        return unicode

    def getIsExtendedHeight(self):
        return self._getBool(1)

    def setIsExtendedHeight(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(FrontlineConfirmIconsModel, self)._initialize()
        self._addArrayProperty('icons', Array())
        self._addBoolProperty('isExtendedHeight', False)