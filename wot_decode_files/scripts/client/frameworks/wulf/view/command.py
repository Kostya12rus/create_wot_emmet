# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/view/command.py
import typing
from Event import Event
from ..py_object_binder import PyObjectEntity
from ..py_object_wrappers import PyObjectCommand

class Command(PyObjectEntity):
    __slots__ = ('__event', )

    def __init__(self):
        super(Command, self).__init__(PyObjectCommand())
        self.__event = Event()

    def __call__(self, args=None):
        if args is not None:
            args = (
             args,)
        else:
            args = ()
        self.__event(*args)
        return

    @property
    def name(self):
        return self.proxy.name

    def execute(self, args=None):
        if args is not None:
            args = (
             args,)
        else:
            args = ()
        self.proxy.execute(*args)
        return

    def _unbind(self):
        self.__event.clear()
        super(Command, self)._unbind()

    def _cNotify(self, args=None):
        if args is not None:
            args = (
             args,)
        else:
            args = ()
        self.__event(*args)
        return

    def __iadd__(self, delegate):
        self.__event += delegate
        return self

    def __isub__(self, delegate):
        self.__event -= delegate
        return self