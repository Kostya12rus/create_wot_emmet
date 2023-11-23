# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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