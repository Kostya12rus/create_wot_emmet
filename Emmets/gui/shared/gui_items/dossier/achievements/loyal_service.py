# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/loyal_service.py
from gui.impl import backport
from gui.shared.gui_items.dossier.achievements.abstract import DeprecatedAchievement
from helpers import i18n

class LoyalServiceAchievement(DeprecatedAchievement):

    def __init__(self, name, block, dossier, value=None):
        super(LoyalServiceAchievement, self).__init__(name, block, dossier, value)
        if dossier is not None:
            self.__registrationDate = backport.getLongDateFormat(dossier.getDossierDescr()['total']['creationTime'])
        else:
            self.__registrationDate = None
        return

    def getUserDescription(self):
        if self.__registrationDate:
            return i18n.makeString(('#achievements:{}_descr').format(self._getActualName()), regDate=self.__registrationDate)
        return ''