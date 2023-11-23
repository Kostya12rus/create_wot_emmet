# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ToolTipMgrMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ToolTipMgrMeta(BaseDAAPIComponent):

    def onCreateComplexTooltip(self, tooltipId, stateType):
        self._printOverrideError('onCreateComplexTooltip')

    def onCreateTypedTooltip(self, tooltipType, args, stateType):
        self._printOverrideError('onCreateTypedTooltip')

    def onHideTooltip(self, tooltipId):
        self._printOverrideError('onHideTooltip')

    def onCreateWulfTooltip(self, tooltipType, args, x, y):
        self._printOverrideError('onCreateWulfTooltip')

    def as_showS(self, tooltipData, linkage, redraw=False):
        if self._isDAAPIInited():
            return self.flashObject.as_show(tooltipData, linkage, redraw)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()