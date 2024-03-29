# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/helpers.py
import typing
if typing.TYPE_CHECKING:
    from uilogging.base.logger import LOGGERS_TYPING

class _LazyLoggerDescriptor(object):
    __slots__ = ('__class', '__args', '__kwargs', '__instance')

    def __init__(self, class_, *args, **kwargs):
        self.__class = class_
        self.__args = args
        self.__kwargs = kwargs
        self.__instance = None
        return

    def __set__(self, *_, **__):
        raise AttributeError('% is readonly' % self.__class__.__name__)

    def __get__(self, *_, **__):
        if not self.__instance:
            self.__instance = self.__class(*self.__args, **self.__kwargs)
        return self.__instance


def lazyUILogger(class_, *args, **kwargs):
    return _LazyLoggerDescriptor(class_, *args, **kwargs)