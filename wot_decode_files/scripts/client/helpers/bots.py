# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/bots.py
import unicodedata, i18n
from constants import ARENA_BONUS_TYPE
from constants import LocalizableBotName, BotNamingType, IS_DEVELOPMENT
from items import tankmen, vehicles
_NAME_FORMAT_CREW_WINBACK = '{0}_{1}'
_NAME_FORMAT_CREW = ':{0} {1}:'
_DEV_PREFIX_FORMAT_CREW = '{0}_{1}_{2} '
_DEV_PREFIX_FORMAT_VEHICLE = '[{0}] '
_DEV_PREFIX_FORMAT_CUSTOM = '[{0}] '

def preprocessBotName(name, arenaBonusType=ARENA_BONUS_TYPE.REGULAR):
    namingType, args = LocalizableBotName.parse(name)
    if namingType == BotNamingType.CREW_MEMBER:
        nationID, firstNameID, lastNameID = args
        nationConfig = tankmen.getNationConfig(nationID)
        firstName = i18n.convert(nationConfig.getFirstName(firstNameID))
        lastName = i18n.convert(nationConfig.getLastName(lastNameID))
        if IS_DEVELOPMENT:
            name = _DEV_PREFIX_FORMAT_CREW.format(nationID, firstNameID, lastNameID) + name
        else:
            if arenaBonusType == ARENA_BONUS_TYPE.WINBACK:
                name = _removeSpecialSymbols(_NAME_FORMAT_CREW_WINBACK.format(firstName, lastName))
            else:
                name = _NAME_FORMAT_CREW.format(firstName, lastName)
    elif namingType == BotNamingType.VEHICLE_MODEL:
        uniqueIndex, nationID, vehicleTypeID = args
        name = i18n.convert(vehicles.g_cache.vehicle(nationID, vehicleTypeID).shortUserString)
        if IS_DEVELOPMENT:
            name = _DEV_PREFIX_FORMAT_VEHICLE.format(uniqueIndex) + name
    elif namingType == BotNamingType.CUSTOM:
        uniqueIndex, stringKey = args
        name = i18n.makeString(stringKey)
        if IS_DEVELOPMENT:
            name = _DEV_PREFIX_FORMAT_CUSTOM.format(uniqueIndex) + name
    return name


def _removeSpecialSymbols(unicodeStr):
    normalized = unicodedata.normalize('NFD', unicodeStr)
    shaved = ('').join(x for x in normalized if not unicodedata.combining(x))
    return i18n.encodeUtf8(unicodedata.normalize('NFC', shaved))