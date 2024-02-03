# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBuffsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBuffsPanelMeta(BaseDAAPIComponent):

    def as_addBuffSlotS(self, idx, imageName, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addBuffSlot(idx, imageName, tooltipText)

    def as_removeBuffSlotS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_removeBuffSlot(idx)