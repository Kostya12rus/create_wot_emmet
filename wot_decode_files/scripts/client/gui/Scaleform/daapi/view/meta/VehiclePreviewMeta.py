# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewMeta.py
from gui.Scaleform.framework.entities.View import View

class VehiclePreviewMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def onBackClick(self):
        self._printOverrideError('onBackClick')

    def onOpenInfoTab(self, index):
        self._printOverrideError('onOpenInfoTab')

    def onCompareClick(self):
        self._printOverrideError('onCompareClick')

    def onGoToPostProgressionClick(self):
        self._printOverrideError('onGoToPostProgressionClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTabsDataS(self, tabs):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsData(tabs)

    def as_show3DSceneTooltipS(self, id, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show3DSceneTooltip(id, args)

    def as_hide3DSceneTooltipS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide3DSceneTooltip()

    def as_setTopPanelS(self, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_setTopPanel(linkage)

    def as_setBottomPanelS(self, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanel(linkage)

    def as_setBulletVisibilityS(self, bulletTabIdx, isBulletVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setBulletVisibility(bulletTabIdx, isBulletVisible)