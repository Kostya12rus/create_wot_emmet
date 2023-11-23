# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/perks_reset_content_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_tankman_model import CrewWidgetTankmanModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_list_model import PriceListModel

class PerksResetContentModel(PriceListModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=1):
        super(PerksResetContentModel, self).__init__(properties=properties, commands=commands)

    def getTankmen(self):
        return self._getArray(1)

    def setTankmen(self, value):
        self._setArray(1, value)

    @staticmethod
    def getTankmenType():
        return CrewWidgetTankmanModel

    def _initialize(self):
        super(PerksResetContentModel, self)._initialize()
        self._addArrayProperty('tankmen', Array())