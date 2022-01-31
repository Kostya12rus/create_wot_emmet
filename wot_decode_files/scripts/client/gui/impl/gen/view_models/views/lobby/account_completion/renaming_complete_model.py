# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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