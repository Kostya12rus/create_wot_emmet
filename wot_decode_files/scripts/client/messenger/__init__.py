# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/__init__.py
import typing
from types import StringType
from external_strings_utils import unicode_from_utf8
from soft_exception import SoftException
from messenger.m_settings import MessengerSettings
if typing.TYPE_CHECKING:
    from types import UnicodeType, IntType

class error(SoftException):
    pass


g_settings = MessengerSettings()

def normalizeGroupId(itemId):
    if isinstance(itemId, StringType):
        return unicode_from_utf8(itemId)[1]
    return itemId