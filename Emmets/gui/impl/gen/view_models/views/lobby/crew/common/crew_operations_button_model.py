# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/crew_operations_button_model.py
from gui.impl.gen.view_models.views.lobby.crew.common.button_model import ButtonModel

class CrewOperationsButtonModel(ButtonModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CrewOperationsButtonModel, self).__init__(properties=properties, commands=commands)

    def getIsAutoReturnOn(self):
        return self._getBool(1)

    def setIsAutoReturnOn(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(CrewOperationsButtonModel, self)._initialize()
        self._addBoolProperty('isAutoReturnOn', False)