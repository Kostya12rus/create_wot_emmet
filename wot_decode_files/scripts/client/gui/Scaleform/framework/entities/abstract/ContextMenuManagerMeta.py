# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContextMenuManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContextMenuManagerMeta(BaseDAAPIComponent):

    def requestOptions(self, type, ctx):
        self._printOverrideError('requestOptions')

    def onOptionSelect(self, optionId):
        self._printOverrideError('onOptionSelect')

    def onHide(self):
        self._printOverrideError('onHide')

    def as_setOptionsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setOptions(data)

    def as_showS(self, type, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show(type, args)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()