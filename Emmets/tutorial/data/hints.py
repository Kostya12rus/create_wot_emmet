# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/data/hints.py
from collections import namedtuple, defaultdict
HintProps = namedtuple('HintProps', ('uniqueID', 'hintID', 'itemID', 'text', 'hasBox',
                                     'arrow', 'padding', 'updateRuntime', 'hideImmediately',
                                     'checkViewArea'))

class HintsData(object):

    def __init__(self):
        super(HintsData, self).__init__()
        self.__guiFilePath = None
        self.__hints = defaultdict(list)
        return

    def getHints(self):
        return self.__hints

    def getHintsCount(self):
        return sum(len(hintsList) for hintsList in self.__hints.itervalues())

    def setGuiFilePath(self, filePath):
        self.__guiFilePath = filePath

    def getGuiFilePath(self):
        return self.__guiFilePath

    def addHint(self, hint):
        self.__hints[hint['itemID']].append(hint)

    def hintsForItem(self, itemID):
        if itemID in self.__hints:
            return self.__hints[itemID]
        return ()

    def markAsShown(self, itemID, hintID):
        if itemID in self.__hints:
            hintsList = self.__hints[itemID]
            self._delHints(hintsList, (hintID,))

    def markHintsAsShown(self, hintIDs):
        for hintsList in self.__hints.itervalues():
            self._delHints(hintsList, hintIDs)

    @staticmethod
    def _delHints(hintsList, ids):
        for idx, hint in reversed(list(enumerate(hintsList))):
            if hint['hintID'] in ids:
                del hintsList[idx]