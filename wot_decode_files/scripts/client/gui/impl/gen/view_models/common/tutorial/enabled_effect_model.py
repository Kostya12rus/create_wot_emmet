# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/enabled_effect_model.py
from gui.impl.gen.view_models.common.tutorial.effect_model import EffectModel

class EnabledEffectModel(EffectModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(EnabledEffectModel, self).__init__(properties=properties, commands=commands)

    def getEnabled(self):
        return self._getBool(4)

    def setEnabled(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(EnabledEffectModel, self)._initialize()
        self._addBoolProperty('enabled', False)