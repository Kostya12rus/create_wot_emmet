# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_cosmic_widget_model.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class ModeSelectorCosmicWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ModeSelectorCosmicWidgetModel, self).__init__(properties=properties, commands=commands)

    def getCurrentProgress(self):
        return self._getNumber(1)

    def setCurrentProgress(self, value):
        self._setNumber(1, value)

    def getTotalCount(self):
        return self._getNumber(2)

    def setTotalCount(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(ModeSelectorCosmicWidgetModel, self)._initialize()
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('totalCount', 0)