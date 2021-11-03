# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/hint_common.py
from visual_script.slot_types import SLOT_TYPE
from visual_script.block import Block
from visual_script.misc import errorVScript
from constants import IS_EDITOR
if not IS_EDITOR:
    from HintManager import HintManager

class ProcessHint(Block):

    def __init__(self, *args, **kwargs):
        super(ProcessHint, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', self.__execute)
        self._id = self._makeDataInputSlot('id', SLOT_TYPE.ID)
        self._out = self._makeEventOutputSlot('out')

    def _processHint(self, hint):
        pass

    def __execute(self):
        if not IS_EDITOR:
            hintId = self._id.getValue()
            hint = HintManager.hintManager().getHint(hintId)
            if hint is not None:
                self._processHint(hint)
            else:
                errorVScript(self, 'Unknown hint id')
        self._out.call()
        return