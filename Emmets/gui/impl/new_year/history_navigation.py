# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/new_year/history_navigation.py


class NavigationHistory(object):

    def __init__(self):
        self.__chain = []
        self.__states = {}
        self.__goingBack = False

    def addToHistory(self, alias, state):
        self.__chain.append(alias)
        self.__states[alias] = state

    def getLast(self, pop=False):
        if self.__chain:
            if pop:
                return self.__chain.pop()
            return self.__chain[(-1)]
        else:
            return

    def pop(self):
        self.__chain.pop()

    def getState(self, viewAlias):
        return self.__states.get(viewAlias)

    def setGoingBack(self, value):
        self.__goingBack = value

    def getGoingBack(self):
        return self.__goingBack

    def invalidateViewState(self, viewAlias):
        if viewAlias not in self.__chain and viewAlias in self.__states:
            del self.__states[viewAlias]

    def remove(self, viewAlias):
        if viewAlias in self.__chain:
            self.__chain.remove(viewAlias)
            del self.__states[viewAlias]

    def clear(self):
        self.__chain = []
        self.__states = {}

    @property
    def isEmpty(self):
        return len(self.__chain) == 0