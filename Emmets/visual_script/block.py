# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/block.py
from typing import List, Any, Sequence
from misc import ASPECT, BLOCK_MODE
from itertools import imap

class EDITOR_TYPE(object):
    STR_KEY_SELECTOR = 1
    ENUM_SELECTOR = 2


def buildStrKeysValue(*args):
    return (';').join(args)


def makeResEditorData(path, *extensions):
    return [
     path, (';;').join(imap((lambda ext: '*.%s' % ext), extensions))]


class InitParam(object):

    def __init__(self, name, slotType, defaultValue, editorType=None, editorData=None):
        self.name = name
        self.slotType = slotType
        self.defaultValue = defaultValue
        self.editorType = editorType
        self.editorData = editorData


class DataInputSlot(object):

    @staticmethod
    def getValue():
        pass

    @staticmethod
    def hasValue():
        return False

    @staticmethod
    def setDefaultValue(value):
        pass

    @staticmethod
    def setEditorData(editorData):
        pass


class DataOutputSlot(object):

    @staticmethod
    def setValue(value):
        pass


class EventInputSlot(object):
    pass


class EventOutputSlot(object):

    @staticmethod
    def call():
        pass


class Meta(object):

    @classmethod
    def blockName(cls):
        return cls.__name__

    @classmethod
    def blockModule(cls):
        return cls.__module__

    @classmethod
    def blockAspects(cls):
        return ASPECT.ALL

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/python'

    @classmethod
    def blockColor(cls):
        return 7189746

    @classmethod
    def blockCategory(cls):
        return 'General'

    @classmethod
    def initParams(cls):
        return []

    @classmethod
    def mode(cls):
        return BLOCK_MODE.NONE


class Block(Meta):

    def __init__(self, agent):
        self.__agent = agent
        super(Block, self).__init__()

    def captionText(self):
        return ''

    @classmethod
    def hasValidation(cls):
        return cls.validate != Block.validate

    def validate(self):
        return ''

    @classmethod
    def isOnFinishScriptCallRequired(cls):
        return cls.onFinishScript != Block.onFinishScript

    def onFinishScript(self):
        pass

    @classmethod
    def isOnStartScriptCallRequired(cls):
        return cls.onStartScript != Block.onStartScript

    def onStartScript(self):
        pass

    def _getInitParams(self):
        return self.__agent.getInitParams()

    def _makeDataInputSlot(self, name, slotType, editorType=-1):
        return self.__agent.makeDataInputSlot(name, slotType, editorType)

    def _makeDataOutputSlot(self, name, slotType, fun):
        return self.__agent.makeDataOutputSlot(name, slotType, fun)

    def _makeEventInputSlot(self, name, fun):
        return self.__agent.makeEventInputSlot(name, fun)

    def _makeEventOutputSlot(self, name):
        return self.__agent.makeEventOutputSlot(name)

    def _writeLog(self, msg):
        self.__agent.writeLog(msg)