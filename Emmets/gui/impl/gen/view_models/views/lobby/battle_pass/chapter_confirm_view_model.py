# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/chapter_confirm_view_model.py
from frameworks.wulf import ViewModel

class ChapterConfirmViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ChapterConfirmViewModel, self).__init__(properties=properties, commands=commands)

    def getPrevChapter(self):
        return self._getNumber(0)

    def setPrevChapter(self, value):
        self._setNumber(0, value)

    def getPrevFinalReward(self):
        return self._getString(1)

    def setPrevFinalReward(self, value):
        self._setString(1, value)

    def getNextChapter(self):
        return self._getNumber(2)

    def setNextChapter(self, value):
        self._setNumber(2, value)

    def getNextFinalReward(self):
        return self._getString(3)

    def setNextFinalReward(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(ChapterConfirmViewModel, self)._initialize()
        self._addNumberProperty('prevChapter', 0)
        self._addStringProperty('prevFinalReward', 'style')
        self._addNumberProperty('nextChapter', 0)
        self._addStringProperty('nextFinalReward', '')