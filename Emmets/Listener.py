# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/Listener.py
import copy, weakref

class Listenable:

    def __init__(self):
        self.listeners = _Listeners()

    def addListener(self, eventName, fn):
        self.listeners.addListener(eventName, fn)

    def removeListener(self, eventName, fn):
        self.listeners.removeListener(eventName, fn)


class _Listeners(object):

    def __init__(self):
        self.listeners = {}

    def addListener(self, eventName, fn):
        if eventName not in self.listeners:
            self.listeners[eventName] = set()
        self.listeners[eventName].add(fn)

    def removeListener(self, eventName, fn):
        if eventName in self.listeners and fn in self.listeners[eventName]:
            self.listeners[eventName].remove(fn)
        if len(self.listeners[eventName]) == 0:
            del self.listeners[eventName]

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return _ListenerDispatch(self, name)


class _ListenerDispatch:

    def __init__(self, dispatcher, eventName):
        self.dispatcher = dispatcher
        self.eventName = eventName

    def __call__(self, *args, **kargs):
        if self.eventName not in self.dispatcher.listeners:
            return
        functions = self.dispatcher.listeners[self.eventName]
        for fn in copy.copy(functions):
            fn(*args, **kargs)


class _ListenerFunc(object):

    def __init__(self, func):
        if hasattr(func, 'im_self'):
            self.isBoundMethod = True
            self.ref = weakref.ref(func.im_self)
            self.func = func.im_func
        else:
            self.isBoundMethod = False
            self.ref = weakref.ref(func)

    def matches(self, func):
        if not self.alive():
            return False
        else:
            if self.isBoundMethod:
                return func == getattr(self.ref(), self.func.func_name)
            return func == self.ref()

    def alive(self):
        return self.ref() is not None

    def get(self):
        obj = self.ref()
        if obj is not None:
            if self.isBoundMethod:
                return getattr(obj, self.func.func_name)
            else:
                return obj

        return

    def __call__(self, *args, **kwargs):
        fn = self.get()
        if fn is not None:
            return fn(*args, **kwargs)
        else:
            return


class FunctionListeners(object):

    def __init__(self):
        self.listeners = []

    def append(self, func):
        self.listeners.append(_ListenerFunc(func))

    def remove(self, func):
        for l in self.listeners:
            if l.matches(func):
                self.listeners.remove(l)
                break

    def reset(self):
        self.listeners = []

    def __call__(self, *args, **kwargs):
        self.listeners = [ l for l in self.listeners if l.alive() ]
        for l in self.listeners:
            l(*args, **kwargs)