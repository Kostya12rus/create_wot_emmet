# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionPanelInjectMeta.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class AmmunitionPanelInjectMeta(InjectComponentAdaptor):

    def onHangarSwitchAnimComplete(self, isComplete):
        self._printOverrideError('onHangarSwitchAnimComplete')

    def as_setPanelSizeS(self, panelWidth, panelHeight, offsetY):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelSize(panelWidth, panelHeight, offsetY)

    def as_setHelpLayoutS(self, helpLayoutData):
        if self._isDAAPIInited():
            return self.flashObject.as_setHelpLayout(helpLayoutData)

    def as_clearHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearHelpLayout()