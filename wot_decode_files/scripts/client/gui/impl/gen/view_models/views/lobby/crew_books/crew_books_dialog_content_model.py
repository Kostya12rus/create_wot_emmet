# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew_books/crew_books_dialog_content_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class CrewBooksDialogContentModel(ViewModel):
    __slots__ = ('onClosed', 'onUseBtnClick')

    def __init__(self, properties=7, commands=2):
        super(CrewBooksDialogContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def crewBookTankmenList(self):
        return self._getViewModel(0)

    @staticmethod
    def getCrewBookTankmenListType():
        return ListModel

    def getIsUseStarted(self):
        return self._getBool(1)

    def setIsUseStarted(self, value):
        self._setBool(1, value)

    def getIsAllCrewIconVisible(self):
        return self._getBool(2)

    def setIsAllCrewIconVisible(self, value):
        self._setBool(2, value)

    def getTitle(self):
        return self._getResource(3)

    def setTitle(self, value):
        self._setResource(3, value)

    def getIcon(self):
        return self._getResource(4)

    def setIcon(self, value):
        self._setResource(4, value)

    def getDescription(self):
        return self._getResource(5)

    def setDescription(self, value):
        self._setResource(5, value)

    def getDescriptionFmtArgs(self):
        return self._getArray(6)

    def setDescriptionFmtArgs(self, value):
        self._setArray(6, value)

    def _initialize(self):
        super(CrewBooksDialogContentModel, self)._initialize()
        self._addViewModelProperty('crewBookTankmenList', ListModel())
        self._addBoolProperty('isUseStarted', False)
        self._addBoolProperty('isAllCrewIconVisible', False)
        self._addResourceProperty('title', R.invalid())
        self._addResourceProperty('icon', R.invalid())
        self._addResourceProperty('description', R.invalid())
        self._addArrayProperty('descriptionFmtArgs', Array())
        self.onClosed = self._addCommand('onClosed')
        self.onUseBtnClick = self._addCommand('onUseBtnClick')