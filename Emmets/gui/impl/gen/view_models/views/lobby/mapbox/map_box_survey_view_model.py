# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/map_box_survey_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_question_model import MapBoxQuestionModel

class MapBoxSurveyViewModel(ViewModel):
    __slots__ = ('onClose', 'onAnswerQuestion', 'onShowPreviousPage', 'onShowNextPage',
                 'onReady')

    def __init__(self, properties=7, commands=5):
        super(MapBoxSurveyViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def question(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestionType():
        return MapBoxQuestionModel

    def getMapId(self):
        return self._getString(1)

    def setMapId(self, value):
        self._setString(1, value)

    def getSurveyGroup(self):
        return self._getString(2)

    def setSurveyGroup(self, value):
        self._setString(2, value)

    def getCurrentPage(self):
        return self._getNumber(3)

    def setCurrentPage(self, value):
        self._setNumber(3, value)

    def getTotalPagesCount(self):
        return self._getNumber(4)

    def setTotalPagesCount(self, value):
        self._setNumber(4, value)

    def getIsSurveyFinish(self):
        return self._getBool(5)

    def setIsSurveyFinish(self, value):
        self._setBool(5, value)

    def getCanContinue(self):
        return self._getBool(6)

    def setCanContinue(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(MapBoxSurveyViewModel, self)._initialize()
        self._addViewModelProperty('question', MapBoxQuestionModel())
        self._addStringProperty('mapId', '')
        self._addStringProperty('surveyGroup', '')
        self._addNumberProperty('currentPage', 0)
        self._addNumberProperty('totalPagesCount', 0)
        self._addBoolProperty('isSurveyFinish', False)
        self._addBoolProperty('canContinue', False)
        self.onClose = self._addCommand('onClose')
        self.onAnswerQuestion = self._addCommand('onAnswerQuestion')
        self.onShowPreviousPage = self._addCommand('onShowPreviousPage')
        self.onShowNextPage = self._addCommand('onShowNextPage')
        self.onReady = self._addCommand('onReady')