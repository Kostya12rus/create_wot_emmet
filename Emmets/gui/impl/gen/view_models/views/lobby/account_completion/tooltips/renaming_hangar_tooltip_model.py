# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/tooltips/renaming_hangar_tooltip_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class RenamingHangarTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RenamingHangarTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getText(self):
        return self._getResource(1)

    def setText(self, value):
        self._setResource(1, value)

    def getTextInner(self):
        return self._getResource(2)

    def setTextInner(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(RenamingHangarTooltipModel, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addResourceProperty('text', R.invalid())
        self._addResourceProperty('textInner', R.invalid())