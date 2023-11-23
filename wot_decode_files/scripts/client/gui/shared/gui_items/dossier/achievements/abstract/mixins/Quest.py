# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/Quest.py
from gui.shared.gui_items.dossier.achievements import validators

class Quest(object):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.questHasThisAchievementAsBonus(name, block) or validators.alreadyAchieved(cls, name, block, dossier)