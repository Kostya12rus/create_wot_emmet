# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/dummy/df_factory.py
from festivity.dummy.df_controller import DummyController
from festivity.dummy.df_processor import DummyCommandsProcessor
from festivity.dummy.df_requester import DummyRequester
from skeletons.festivity_factory import IFestivityFactory

class DummyFactory(IFestivityFactory):

    def __init__(self):
        super(DummyFactory, self).__init__()
        self.__requester = DummyRequester()
        self.__processor = DummyCommandsProcessor()
        self.__controller = DummyController()

    def getRequester(self):
        return self.__requester

    def getProcessor(self):
        return self.__processor

    def getController(self):
        return self.__controller

    def getDataSyncKey(self):
        return 'dummySyncKey'