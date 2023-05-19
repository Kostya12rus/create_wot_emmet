# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/WeakMixin.py
import new, weakref
from inspect import getmodule

class Tapped(object):
    __slots__ = ()

    def tap(self, *appliers, **props):
        for applier in appliers:
            if callable(applier):
                applier(self)

        for p, v in props.iteritems():
            try:
                setattr(self, p, v)
            except (AttributeError, TypeError):
                pass

        return self


class WeakMixin(object):

    def __new__(cls, src, *args, **kwargs):
        kls = None
        srcKlass = src.__class__
        for k in cls.__subclasses__():
            if issubclass(k, srcKlass):
                kls = k
                break

        if not kls:
            mixinName = ('_{}_weakMixin').format(srcKlass.__name__)
            module = getmodule(cls)
            kls = new.classobj(mixinName, (cls, srcKlass), {})
            if module is not None:
                setattr(module, mixinName, kls)
        obj = object.__new__(kls)
        obj.__target__ = weakref.proxy(src)
        return obj

    def __init__(self, src, *args, **kwargs):
        pass

    def __getattribute__(self, name):
        ogetattribute = object.__getattribute__
        try:
            return ogetattribute(self, name)
        except AttributeError:
            return self.__target__.__getattribute__(name)