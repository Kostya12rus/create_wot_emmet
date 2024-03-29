# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/common/field_name_model.py
from enum import IntEnum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_field_model import BaseFieldModel

class NameStateEnum(IntEnum):
    UNDEFINED = 0
    CHECKING = 1
    OK = 2
    ERROR = 3


class FieldNameModel(BaseFieldModel):
    __slots__ = ('onSuggestionSelected', )
    NAME_LEN_MAX = 24
    NAME_LEN_MIN = 3

    def __init__(self, properties=6, commands=3):
        super(FieldNameModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return NameStateEnum(self._getNumber(4))

    def setState(self, value):
        self._setNumber(4, value.value)

    def getSuggestions(self):
        return self._getArray(5)

    def setSuggestions(self, value):
        self._setArray(5, value)

    @staticmethod
    def getSuggestionsType():
        return unicode

    def _initialize(self):
        super(FieldNameModel, self)._initialize()
        self._addNumberProperty('state')
        self._addArrayProperty('suggestions', Array())
        self.onSuggestionSelected = self._addCommand('onSuggestionSelected')