# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/migration/proxy.py


class MigrationProxy(object):
    __slots__ = ('_proto', )

    def __init__(self, proto):
        super(MigrationProxy, self).__init__()
        self._proto = proto

    def clear(self):
        self._proto = None
        return