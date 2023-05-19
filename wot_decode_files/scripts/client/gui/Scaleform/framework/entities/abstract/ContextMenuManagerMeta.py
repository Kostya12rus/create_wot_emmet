# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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