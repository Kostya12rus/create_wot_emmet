# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/general.py
from block import Block, makeResEditorData, InitParam
from slot_types import SLOT_TYPE
from uuid_utils import genUUID

class ResourceSelector(Block):

    def __init__(self, *args, **kwargs):
        super(ResourceSelector, self).__init__(*args, **kwargs)
        root, ext = self._getInitParams()
        self._res = self._makeDataInputSlot('res', SLOT_TYPE.RESOURCE)
        self._res.setEditorData(makeResEditorData(root, ext))
        self._out = self._makeDataOutputSlot('out', SLOT_TYPE.RESOURCE, self._exec)

    def _exec(self):
        self._out.setValue(self._res.getValue())

    @classmethod
    def initParams(cls):
        return [InitParam('root', SLOT_TYPE.STR, 'wot'), InitParam('ext', SLOT_TYPE.STR, 'xml')]


class GenerateUniqueString(Block):

    def __init__(self, *args, **kwargs):
        super(GenerateUniqueString, self).__init__(*args, **kwargs)
        self._prefix = self._makeDataInputSlot('prefix', SLOT_TYPE.STR)
        self._res = self._makeDataOutputSlot('res', SLOT_TYPE.STR, self._getData)

    @classmethod
    def hasValidation(cls):
        return True

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/text'

    @classmethod
    def blockCategory(cls):
        return 'Strings'

    def _getData(self):
        prefix = self._prefix.getValue() if self._prefix.hasValue() else ''
        self._res.setValue(('{prefix}_{ts}').format(prefix=prefix, ts=genUUID().time))