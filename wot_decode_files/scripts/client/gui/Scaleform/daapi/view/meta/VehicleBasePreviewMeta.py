# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleBasePreviewMeta.py
from gui.Scaleform.framework.entities.View import View

class VehicleBasePreviewMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def onBackClick(self):
        self._printOverrideError('onBackClick')

    def onOpenInfoTab(self, index):
        self._printOverrideError('onOpenInfoTab')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setAdditionalInfoS(self, info):
        if self._isDAAPIInited():
            return self.flashObject.as_setAdditionalInfo(info)

    def as_show3DSceneTooltipS(self, id, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show3DSceneTooltip(id, args)

    def as_hide3DSceneTooltipS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide3DSceneTooltip()

    def as_setBottomPanelS(self, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanel(linkage)