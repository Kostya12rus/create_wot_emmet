# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleAmmunitionPanelViewMeta.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class PrebattleAmmunitionPanelViewMeta(InjectComponentAdaptor):

    def onViewIsHidden(self):
        self._printOverrideError('onViewIsHidden')

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()

    def as_hideS(self, useAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(useAnim)

    def as_setIsInLoadingS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsInLoading(value)