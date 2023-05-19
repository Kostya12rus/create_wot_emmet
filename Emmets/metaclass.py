# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/metaclass.py


class Metaclass(type):

    def __init__(cls, name, bases, attrs):
        mro = list(cls.__mro__)
        mro.pop(0)
        for base in reversed(mro):
            init = base.__dict__.get('__init_subclass__', None)
            if init:
                init.__func__(cls, name, bases, attrs)

        return