# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/map_box_option_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_answers_model import MapBoxAnswersModel

class MapBoxOptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MapBoxOptionModel, self).__init__(properties=properties, commands=commands)

    @property
    def answers(self):
        return self._getViewModel(0)

    @staticmethod
    def getAnswersType():
        return MapBoxAnswersModel

    def getOptionId(self):
        return self._getString(1)

    def setOptionId(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(MapBoxOptionModel, self)._initialize()
        self._addViewModelProperty('answers', MapBoxAnswersModel())
        self._addStringProperty('optionId', '')