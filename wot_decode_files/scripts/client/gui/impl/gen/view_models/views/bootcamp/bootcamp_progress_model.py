# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/bootcamp/bootcamp_progress_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.bootcamp.bootcamp_lesson_model import BootcampLessonModel

class BootcampProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BootcampProgressModel, self).__init__(properties=properties, commands=commands)

    def getCurrentLesson(self):
        return self._getNumber(0)

    def setCurrentLesson(self, value):
        self._setNumber(0, value)

    def getTotalLessons(self):
        return self._getNumber(1)

    def setTotalLessons(self, value):
        self._setNumber(1, value)

    def getIsNeedAwarding(self):
        return self._getBool(2)

    def setIsNeedAwarding(self, value):
        self._setBool(2, value)

    def getLevels(self):
        return self._getArray(3)

    def setLevels(self, value):
        self._setArray(3, value)

    @staticmethod
    def getLevelsType():
        return BootcampLessonModel

    def _initialize(self):
        super(BootcampProgressModel, self)._initialize()
        self._addNumberProperty('currentLesson', 0)
        self._addNumberProperty('totalLessons', 0)
        self._addBoolProperty('isNeedAwarding', False)
        self._addArrayProperty('levels', Array())