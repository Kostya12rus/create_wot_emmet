# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/icon_view_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class IconViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(IconViewModel, self).__init__(properties=properties, commands=commands)

    def getPath(self):
        return self._getResource(0)

    def setPath(self, value):
        self._setResource(0, value)

    def _initialize(self):
        super(IconViewModel, self)._initialize()
        self._addResourceProperty('path', R.invalid())