# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/common/field_password_model.py
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_field_model import BaseFieldModel

class FieldPasswordModel(BaseFieldModel):
    __slots__ = ('onEyeClicked', )
    PASSWORD_LEN_MAX = 100
    PASSWORD_LEN_MIN = 8

    def __init__(self, properties=5, commands=3):
        super(FieldPasswordModel, self).__init__(properties=properties, commands=commands)

    def getIsPasswordVisible(self):
        return self._getBool(4)

    def setIsPasswordVisible(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(FieldPasswordModel, self)._initialize()
        self._addBoolProperty('isPasswordVisible', False)
        self.onEyeClicked = self._addCommand('onEyeClicked')