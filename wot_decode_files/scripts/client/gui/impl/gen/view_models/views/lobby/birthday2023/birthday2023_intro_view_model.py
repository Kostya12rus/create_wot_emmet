# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/birthday2023/birthday2023_intro_view_model.py
from frameworks.wulf import ViewModel

class Birthday2023IntroViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=0, commands=1):
        super(Birthday2023IntroViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(Birthday2023IntroViewModel, self)._initialize()
        self.onClose = self._addCommand('onClose')