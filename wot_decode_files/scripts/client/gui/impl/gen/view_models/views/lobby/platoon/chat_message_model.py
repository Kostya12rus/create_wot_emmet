# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/chat_message_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.chat_message_part_model import ChatMessagePartModel

class ChatMessageModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ChatMessageModel, self).__init__(properties=properties, commands=commands)

    @property
    def playerName(self):
        return self._getViewModel(0)

    @staticmethod
    def getPlayerNameType():
        return ChatMessagePartModel

    @property
    def timeStamp(self):
        return self._getViewModel(1)

    @staticmethod
    def getTimeStampType():
        return ChatMessagePartModel

    @property
    def text(self):
        return self._getViewModel(2)

    @staticmethod
    def getTextType():
        return ChatMessagePartModel

    def getKey(self):
        return self._getNumber(3)

    def setKey(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(ChatMessageModel, self)._initialize()
        self._addViewModelProperty('playerName', ChatMessagePartModel())
        self._addViewModelProperty('timeStamp', ChatMessagePartModel())
        self._addViewModelProperty('text', ChatMessagePartModel())
        self._addNumberProperty('key', 0)