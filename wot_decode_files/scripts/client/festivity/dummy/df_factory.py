# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/dummy/df_factory.py
from festivity.dummy.df_controller import DummyController
from festivity.dummy.df_processor import DummyCommandsProcessor
from festivity.dummy.df_requester import DummyRequester
from skeletons.festivity_factory import IFestivityFactory

class DummyFactory(IFestivityFactory):

    def __init__(self):
        self.__requester = DummyRequester()
        self.__processor = DummyCommandsProcessor()
        self.__controller = DummyController()

    def getRequester(self):
        return self.__requester

    def getProcessor(self):
        return self.__processor

    def getController(self):
        return self.__controller