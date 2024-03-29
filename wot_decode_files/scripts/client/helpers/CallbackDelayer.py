# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/CallbackDelayer.py
import functools, BigWorld

class CallbackDelayer(object):

    def __init__(self):
        self.__callbacks = {}

    def destroy(self):
        self.clearCallbacks()

    def clearCallbacks(self):
        for _, callbackId in self.__callbacks.iteritems():
            if callbackId is not None:
                BigWorld.cancelCallback(callbackId)

        self.__callbacks = {}
        return

    def __funcWrapper(self, func, *args, **kwargs):
        del self.__callbacks[func]
        desiredDelay = func(*args, **kwargs)
        if desiredDelay is not None and desiredDelay >= 0:
            curId = BigWorld.callback(desiredDelay, functools.partial(self.__funcWrapper, func, *args, **kwargs))
            self.__callbacks[func] = curId
        return

    def delayCallback(self, seconds, func, *args, **kwargs):
        curId = self.__callbacks.get(func)
        if curId is not None:
            BigWorld.cancelCallback(curId)
            del self.__callbacks[func]
        curId = BigWorld.callback(seconds, functools.partial(self.__funcWrapper, func, *args, **kwargs))
        self.__callbacks[func] = curId
        return

    def stopCallback(self, func):
        curId = self.__callbacks.get(func)
        if curId is not None:
            BigWorld.cancelCallback(curId)
            del self.__callbacks[func]
        return

    def hasDelayedCallback(self, func):
        return func in self.__callbacks


class CallbacksSetByID(object):
    __slots__ = ('__callbackIDs', )

    def __init__(self):
        super(CallbacksSetByID, self).__init__()
        self.__callbackIDs = {}

    def clear(self):
        while self.__callbackIDs:
            _, callbackID = self.__callbackIDs.popitem()
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        return

    def delayCallback(self, uniqueID, seconds, function, *args, **kwargs):
        self.stopCallback(uniqueID)
        self.__callbackIDs[uniqueID] = BigWorld.callback(seconds, functools.partial(self.__funcWrapper, uniqueID, function, *args, **kwargs))

    def stopCallback(self, uniqueID):
        callbackID = self.__callbackIDs.pop(uniqueID, None)
        if callbackID is not None:
            BigWorld.cancelCallback(callbackID)
        return

    def hasDelayedCallbackID(self, uniqueID):
        return uniqueID in self.__callbackIDs

    def __funcWrapper(self, uniqueID, func, *args, **kwargs):
        self.__callbackIDs[uniqueID] = None
        func(*args, **kwargs)
        return


class TimeDeltaMeter(object):

    def __init__(self, timeFunc=BigWorld.time):
        self.__timeFunc = timeFunc
        self.__prevTime = timeFunc()

    def measureDeltaTime(self):
        time = self.__timeFunc()
        deltaTime = time - self.__prevTime
        self.__prevTime = time
        return deltaTime