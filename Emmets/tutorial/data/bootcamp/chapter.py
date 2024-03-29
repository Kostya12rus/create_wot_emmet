# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/data/bootcamp/chapter.py
from tutorial.data.chapter import Chapter

class BootcampLobbyChapter(Chapter):

    def __init__(self, sharedTriggers, sharedVars, *args, **kwargs):
        super(BootcampLobbyChapter, self).__init__(*args, **kwargs)
        self.__sharedTriggersPath = sharedTriggers
        self.__sharedVarsPath = sharedVars

    def getSharedTriggersPath(self):
        return self.__sharedTriggersPath

    def getSharedVarsPath(self):
        return self.__sharedVarsPath