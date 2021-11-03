# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/stage.py
from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_TYPE

class StageAchievement(RegularAchievement):
    __slots__ = ()

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return cls.checkIsInDossier(block, name, dossier)

    def getType(self):
        return ACHIEVEMENT_TYPE.SINGLE

    def _getActualName(self):
        return '%s%d' % (self._name, self._value)