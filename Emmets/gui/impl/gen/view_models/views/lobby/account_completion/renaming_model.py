# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/renaming_model.py
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_wgnp_overlay_view_model import BaseWgnpOverlayViewModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.field_name_model import FieldNameModel

class RenamingModel(BaseWgnpOverlayViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=4):
        super(RenamingModel, self).__init__(properties=properties, commands=commands)

    @property
    def name(self):
        return self._getViewModel(9)

    @staticmethod
    def getNameType():
        return FieldNameModel

    def _initialize(self):
        super(RenamingModel, self)._initialize()
        self._addViewModelProperty('name', FieldNameModel())