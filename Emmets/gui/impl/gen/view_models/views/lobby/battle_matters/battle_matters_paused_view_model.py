# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_paused_view_model.py
from frameworks.wulf import ViewModel

class BattleMattersPausedViewModel(ViewModel):
    __slots__ = ('gotoHangar', )

    def __init__(self, properties=0, commands=1):
        super(BattleMattersPausedViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(BattleMattersPausedViewModel, self)._initialize()
        self.gotoHangar = self._addCommand('gotoHangar')