# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/managers/UtilsManager.py
import calendar, Keys
from Keys import KEY_NONE
from gui.Scaleform.framework.managers.TextManager import TextManager
from gui.Scaleform.locale.MENU import MENU
from gui.shared.utils.functions import getAbsoluteUrl
import nations, BigWorld
from gui import GUI_NATIONS
from gui.shared import utils
from gui.Scaleform.framework.entities.abstract.UtilsManagerMeta import UtilsManagerMeta
from gui.shared.utils.key_mapping import SCALEFORM_TO_BW, canGetVirtualKey, BW_TO_SCALEFORM, MappingType
from helpers import i18n, getClientLanguage
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
ONE_SECOND = 1

class UtilsManager(UtilsManagerMeta):

    def __init__(self):
        super(UtilsManager, self).__init__()
        self._textMgr = TextManager()

    def registerTextManager(self, flashObject):
        self._textMgr.setFlashObject(flashObject)

    def destroy(self):
        self.__unregisterMrgs()
        super(UtilsManagerMeta, self).destroy()

    def __unregisterMrgs(self):
        self._textMgr.destroy()
        self._textMgr = None
        return

    def __isKeyboardKey(self, inKey):
        return inKey > BW_TO_SCALEFORM[Keys.KEY_MOUSE7]

    @property
    def textManager(self):
        return self._textMgr

    def getGUINations(self):
        return GUI_NATIONS

    def getNationNames(self):
        return nations.NAMES

    def mapScaleformToVirtualKey(self, inKey):
        if inKey not in SCALEFORM_TO_BW or not self.__isKeyboardKey(inKey):
            return inKey
        tkey = SCALEFORM_TO_BW[inKey]
        if tkey == KEY_NONE or not canGetVirtualKey(tkey):
            return inKey
        return BigWorld.mapVirtualKey(tkey, MappingType.MAPVK_VSC_TO_VK)

    def getCharFromVirtualKey(self, key):
        return BigWorld.mapVirtualKey(key, MappingType.MAPVK_VK_TO_CHAR)

    def getNationIndices(self):
        return nations.INDICES

    def changeStringCasing(self, s, isUpper, _):
        return utils.changeStringCasing(str(s).decode('utf-8'), isUpper)

    @classmethod
    def getAbsoluteUrl(cls, value):
        return getAbsoluteUrl(value)

    @classmethod
    def getHtmlIconText(cls, properties):
        template = "<img src='{0}' width='{1}' height='{2}' vspace='{3}' hspace='{4}'/>"
        absoluteUrl = cls.getAbsoluteUrl(properties.imageAlias)
        return template.format(absoluteUrl, properties.width, properties.height, properties.vSpace, properties.hSpace)

    def getFirstDayOfWeek(self):
        return BigWorld.wg_firstDayOfWeek() + 1

    def getWeekDayNames(self, full, isUpper, isLower, useRegionSettings=True):
        source = list(MENU.DATETIME_WEEKDAYS_FULL_ENUM if full else MENU.DATETIME_WEEKDAYS_SHORT_ENUM)
        result = []
        if useRegionSettings:
            firstDayOfWeek = BigWorld.wg_firstDayOfWeek()
        else:
            firstDayOfWeek = 0
        for day in calendar.Calendar(firstweekday=firstDayOfWeek).iterweekdays():
            name = i18n.makeString(source[day])
            if isUpper:
                name = self.changeStringCasing(name, True, None)
            elif isLower:
                name = self.changeStringCasing(name, False, None)
            result.append(name)

        return result

    def getMonthsNames(self, full, isUpper, isLower):
        source = list(MENU.DATETIME_MONTHS_FULL_ENUM if full else MENU.DATETIME_MONTHS_SHORT_ENUM)
        result = []
        for key in source:
            name = i18n.makeString(key)
            if isUpper:
                name = self.changeStringCasing(name, True, None)
            elif isLower:
                name = self.changeStringCasing(name, False, None)
            result.append(name)

        return result

    def _dispose(self):
        self._textMgr = None
        super(UtilsManager, self)._dispose()
        return

    def intToStringWithPrefixPatern(self, value, count, fill):
        return ('{0:' + str(fill) + '>' + str(count) + '}').format(value)

    def isTwelveHoursFormat(self):
        return getClientLanguage() == 'en'


class ImageUrlProperties(object):

    def __init__(self, imageAlias, width=16, height=16, vSpace=-4, hSpace=0):
        super(ImageUrlProperties, self).__init__()
        self.imageAlias = imageAlias
        self.width = width
        self.height = height
        self.vSpace = vSpace
        self.hSpace = hSpace