# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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