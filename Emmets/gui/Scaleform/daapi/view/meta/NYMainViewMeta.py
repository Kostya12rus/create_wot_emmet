# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NYMainViewMeta.py
from gui.Scaleform.framework.entities.View import View

class NYMainViewMeta(View):

    def onEscPress(self):
        self._printOverrideError('onEscPress')

    def onSwitchView(self):
        self._printOverrideError('onSwitchView')

    def as_switchViewS(self, toInject):
        if self._isDAAPIInited():
            return self.flashObject.as_switchView(toInject)