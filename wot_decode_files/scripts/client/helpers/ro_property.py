# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/ro_property.py


def getMethod(name):

    def _getMethod(self):
        return self.__readonly__[name]

    return _getMethod


class ROPropertyMeta(type):

    def __new__(mcs, className, bases, classDict):
        readonly = classDict.get('__readonly__', {})
        for name, _ in readonly.items():
            classDict[name] = property(getMethod(name))

        return type.__new__(mcs, className, bases, classDict)