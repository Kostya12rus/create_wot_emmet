# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/ValueTracker.py
import math, functools, GUI, constants
from helpers.CallbackDelayer import CallbackDelayer

class ValueTracker(CallbackDelayer):
    _ENABLED = True and constants.IS_DEVELOPMENT
    __instance = None
    textGui = property((lambda self: self.__textGui if constants.IS_DEVELOPMENT else None))

    @staticmethod
    def enable(isEnable):
        ValueTracker._ENABLED = constants.IS_DEVELOPMENT and isEnable
        if constants.IS_DEVELOPMENT:
            ValueTracker.instance().textGui.visible = ValueTracker._ENABLED

    @staticmethod
    def instance():
        if ValueTracker.__instance is None:
            ValueTracker.__instance = ValueTracker()
        return ValueTracker.__instance

    def __init__(self):
        if not constants.IS_DEVELOPMENT:
            return
        CallbackDelayer.__init__(self)
        self.__items = {}
        self.__avgInfo = {}
        self.__textGui = GUI.Text()
        GUI.addRoot(self.__textGui)
        self.__textGui.position = (0, -0.25, 0)
        self.__textGui.multiline = True
        self.clear()
        self.__tickNames = {}

    def destroy(self):
        if not constants.IS_DEVELOPMENT:
            return
        GUI.delRoot(self.__textGui)

    def clear(self):
        if not constants.IS_DEVELOPMENT:
            return
        self.__textGui.text = ''

    def addValue(self, name, value):
        if not ValueTracker._ENABLED:
            return
        self.__items[name] = value
        self.__updateText()

    def addValue2(self, name, value):
        if not ValueTracker._ENABLED:
            return
        self.__items[name] = math.floor(value * 1000) / 1000
        self.__updateText()

    def addValueAverage(self, name, value, maxAmount=100):
        curSum, curAm = self.__avgInfo.get(name, (None, 0))
        if curAm < maxAmount:
            curSum = curSum + value if curSum is not None else value
            self.__avgInfo[name] = (curSum, curAm + 1)
        else:
            self.addValue(name, curSum / curAm)
            self.__avgInfo[name] = (value, 1)
        return

    def addValueTick(self, name, callback, period):
        func = functools.partial(self.__tickFunc, name, callback, period)
        self.__tickNames[name] = func
        self.delayCallback(period, func)

    def removeValueTick(self, name):
        func = self.__tickNames.get(name)
        if func:
            self.stopCallback(func)

    def __tickFunc(self, name, callback, period):
        try:
            self.addValue(name, callback())
        except Exception:
            return -1

        return period

    def __updateText(self):
        text = ''
        for n, v in self.__items.iteritems():
            text += '%s: %s\n' % (n, str(v))

        self.__textGui.text = text