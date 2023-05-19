# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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