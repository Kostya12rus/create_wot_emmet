# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/complete_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class CompleteModel(BaseOverlayViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=2):
        super(CompleteModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(2)

    def setTitle(self, value):
        self._setResource(2, value)

    def getSubTitle(self):
        return self._getResource(3)

    def setSubTitle(self, value):
        self._setResource(3, value)

    def _initialize(self):
        super(CompleteModel, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addResourceProperty('subTitle', R.invalid())