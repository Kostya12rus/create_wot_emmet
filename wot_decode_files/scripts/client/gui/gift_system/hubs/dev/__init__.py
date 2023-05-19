# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/hubs/dev/__init__.py
from gui import SystemMessages
from gui.shared.formatters import text_styles

class IDevMessagesPusher(object):

    @classmethod
    def _formatMessage(cls, message):
        return text_styles.stats(message)

    @classmethod
    def _pushClientMessage(cls, message):
        SystemMessages.pushMessage(cls._formatMessage(message), SystemMessages.SM_TYPE.MediumInfo)