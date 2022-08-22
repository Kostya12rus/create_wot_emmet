# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/icon_set_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel

class IconSetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(IconSetViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def icon(self):
        return self._getViewModel(0)

    @staticmethod
    def getIconType():
        return IconViewModel

    def getBackgrounds(self):
        return self._getArray(1)

    def setBackgrounds(self, value):
        self._setArray(1, value)

    @staticmethod
    def getBackgroundsType():
        return IconViewModel

    def getOverlays(self):
        return self._getArray(2)

    def setOverlays(self, value):
        self._setArray(2, value)

    @staticmethod
    def getOverlaysType():
        return IconViewModel

    def _initialize(self):
        super(IconSetViewModel, self)._initialize()
        self._addViewModelProperty('icon', IconViewModel())
        self._addArrayProperty('backgrounds', Array())
        self._addArrayProperty('overlays', Array())