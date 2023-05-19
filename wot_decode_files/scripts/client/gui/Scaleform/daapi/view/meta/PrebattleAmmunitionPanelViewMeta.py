# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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

    def as_showShadowsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showShadows(value)