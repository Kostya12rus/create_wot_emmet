# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/web/storage.py


class IStorage(object):

    def close(self):
        raise NotImplementedError

    def add(self, name, data, callback):
        raise NotImplementedError

    def remove(self, name):
        raise NotImplementedError

    def isStored(self, name):
        raise NotImplementedError

    def getAll(self):
        raise NotImplementedError