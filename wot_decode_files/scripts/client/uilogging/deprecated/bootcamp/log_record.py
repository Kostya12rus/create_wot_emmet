# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/deprecated/bootcamp/log_record.py
from uilogging.core.log import LogRecord

class BootcampLogRecord(LogRecord):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(BootcampLogRecord, self).__init__(*args, **kwargs)
        if self._properties:
            self._properties.setdefault('is_newbie', None)
            self._properties.setdefault('lesson_id', None)
            self._properties.setdefault('finishReason', None)
            self._properties.setdefault('item_id', None)
            self._properties.setdefault('skipped', None)
            self._properties.setdefault('page', None)
            self._properties.setdefault('tooltip', None)
            intProperties = ('lesson_id', 'item_id', 'page')
            for propertyName in intProperties:
                if propertyName in self._properties and self._properties[propertyName] is not None:
                    self._properties[propertyName] = int(self._properties[propertyName])

        return