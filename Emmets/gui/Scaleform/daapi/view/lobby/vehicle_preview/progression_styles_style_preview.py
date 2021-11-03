# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/progression_styles_style_preview.py
from gui.Scaleform.daapi.view.lobby.vehicle_preview.style_preview import VehicleStylePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS

class ProgressionStylesStylePreview(VehicleStylePreview):

    def __init__(self, ctx=None):
        super(ProgressionStylesStylePreview, self).__init__(ctx)
        self.__styleLevel = ctx.get('styleLevel')

    def setBottomPanel(self, linkage=None):
        self.as_setBottomPanelS(linkage)

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(ProgressionStylesStylePreview, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VEHPREVIEW_CONSTANTS.PROGRESSION_STYLES_BUYING_PANEL_PY_ALIAS:
            viewPy.setStyleLevel(self.__styleLevel)

    def _populate(self):
        self.setBottomPanel(VEHPREVIEW_CONSTANTS.PROGRESSION_STYLES_BUYING_PANEL_LINKAGE)
        super(ProgressionStylesStylePreview, self)._populate()