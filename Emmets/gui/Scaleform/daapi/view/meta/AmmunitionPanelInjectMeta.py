# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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