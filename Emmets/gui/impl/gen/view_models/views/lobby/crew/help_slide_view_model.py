# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/help_slide_view_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.help_slide_section_view_model import HelpSlideSectionViewModel

class HelpSlideViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(HelpSlideViewModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getSections(self):
        return self._getArray(1)

    def setSections(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSectionsType():
        return HelpSlideSectionViewModel

    def _initialize(self):
        super(HelpSlideViewModel, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addArrayProperty('sections', Array())