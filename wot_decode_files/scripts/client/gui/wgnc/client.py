# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/client.py
from gui.wgnc.settings import WGNC_GUI_TYPE

class ClosePollWindowFromPopUp(object):
    __slots__ = ('_target', )

    def __init__(self, target):
        super(ClosePollWindowFromPopUp, self).__init__()
        self._target = target

    def process(self, actor, notID, actions, items):
        if actor.getType() != WGNC_GUI_TYPE.POP_UP:
            return
        submit = actor.getSubmitButton()
        if not submit:
            return
        if submit.action != actions:
            return
        item = items.getItemByName(self._target)
        if item:
            item.close(notID)


class ClientLogic(object):
    __slots__ = ('_seq', )

    def __init__(self, seq):
        super(ClientLogic, self).__init__()
        self._seq = seq

    def process(self, actor, notID, actions, items):
        for logic in self._seq:
            logic.process(actor, notID, actions, items)