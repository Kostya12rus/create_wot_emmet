# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/common/keybord_helpers.py
import BigWorld, CommandMapping
from gui.Scaleform.locale.READABLE_KEY_NAMES import READABLE_KEY_NAMES
from helpers.i18n import makeString

def getHotKeyList(command):
    keys = []
    key, satelliteKeys = CommandMapping.g_instance.getCommandKeys(command)
    for satelliteKey in satelliteKeys:
        keys.append(makeString(READABLE_KEY_NAMES.key(BigWorld.keyToString(satelliteKey))))

    keys.append(makeString(READABLE_KEY_NAMES.key(BigWorld.keyToString(key))))
    return keys