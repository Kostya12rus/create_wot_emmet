# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/compare_modification_model.py
from gui.impl.gen.view_models.views.lobby.post_progression.base_modification_model import BaseModificationModel

class CompareModificationModel(BaseModificationModel):
    __slots__ = ()
    UNDEFINED = -1

    def __init__(self, properties=5, commands=0):
        super(CompareModificationModel, self).__init__(properties=properties, commands=commands)

    def getParentStepId(self):
        return self._getNumber(4)

    def setParentStepId(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(CompareModificationModel, self)._initialize()
        self._addNumberProperty('parentStepId', 0)