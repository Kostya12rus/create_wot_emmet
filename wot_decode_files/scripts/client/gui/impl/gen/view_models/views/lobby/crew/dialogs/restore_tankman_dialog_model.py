# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/restore_tankman_dialog_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class RestoreTankmanDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=2):
        super(RestoreTankmanDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def tankman(self):
        return self._getViewModel(6)

    @staticmethod
    def getTankmanType():
        return TankmanModel

    def _initialize(self):
        super(RestoreTankmanDialogModel, self)._initialize()
        self._addViewModelProperty('tankman', TankmanModel())