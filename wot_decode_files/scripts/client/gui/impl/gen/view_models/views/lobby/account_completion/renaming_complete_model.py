# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/renaming_complete_model.py
from gui.impl.gen.view_models.views.lobby.account_completion.complete_model import CompleteModel

class RenamingCompleteModel(CompleteModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=2):
        super(RenamingCompleteModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(4)

    def setName(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(RenamingCompleteModel, self)._initialize()
        self._addStringProperty('name', '')