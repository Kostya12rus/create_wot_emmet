# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/mark_on_gun.py
from gui.impl import backport
from helpers import i18n
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui import makeHtmlString
from abstract import RegularAchievement
from items import vehicles
from nations import NAMES as NATION_NAMES

class MarkOnGunAchievement(RegularAchievement):
    __slots__ = ('__nationId', '__damageRating')
    IT_95X85 = '95x85'

    def __init__(self, dossier, value=None):
        super(MarkOnGunAchievement, self).__init__('marksOnGun', _AB.TOTAL, dossier, value)
        self.__nationId = self._readVehicleNationID(dossier)
        self.__damageRating = self._readDamageRating(dossier)

    def setVehicleNationID(self, nationID):
        self.__nationId = nationID

    def getVehicleNationID(self):
        return self.__nationId

    def getUserCondition(self):
        return i18n.makeString('#achievements:marksOnGun_condition')

    def setDamageRating(self, val):
        self.__damageRating = val

    def getDamageRating(self):
        return self.__damageRating

    def getIcons(self):
        return {self.ICON_TYPE.IT_180X180: self.__getIconPath(self.ICON_TYPE.IT_180X180), 
           self.ICON_TYPE.IT_67X71: self.__getIconPath(self.ICON_TYPE.IT_67X71), 
           self.ICON_TYPE.IT_32X32: self.__getIconPath(self.ICON_TYPE.IT_32X32), 
           self.IT_95X85: self.__getIconPath(self.IT_95X85)}

    def getI18nValue(self):
        if self.__damageRating > 0:
            return makeHtmlString('html_templates:lobby/tooltips/achievements', 'marksOnGun', {'count': backport.getNiceNumberFormat(self.__damageRating)})
        return ''

    def _getActualName(self):
        return '%s%d' % (self._name, self._value)

    @classmethod
    def _readDamageRating(cls, dossier):
        if dossier is not None:
            return dossier.getRecordValue(_AB.TOTAL, 'damageRating') / 100.0
        else:
            return 0.0

    @classmethod
    def _readVehicleNationID(cls, dossier):
        if dossier is not None:
            return vehicles.parseIntCompactDescr(dossier.getCompactDescriptor())[1]
        else:
            return 0

    def __getIconPath(self, dir_):
        currentValue = 3 if self._value == 0 else self._value
        markCtx = 'mark' if currentValue < 2 else 'marks'
        return '../maps/icons/marksOnGun/%s/%s_%s_%s.png' % (dir_, NATION_NAMES[self.__nationId],
         currentValue, markCtx)

    def __repr__(self):
        return 'MarkOnGunAchievement<value=%s; damageRating=%.2f>' % (
         str(self._value), float(self.__damageRating))