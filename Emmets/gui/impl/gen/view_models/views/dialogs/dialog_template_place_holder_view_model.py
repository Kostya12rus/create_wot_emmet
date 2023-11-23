# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/dialog_template_place_holder_view_model.py
from frameworks.wulf import ViewModel

class DialogTemplatePlaceHolderViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DialogTemplatePlaceHolderViewModel, self).__init__(properties=properties, commands=commands)

    def getResourceID(self):
        return self._getNumber(0)

    def setResourceID(self, value):
        self._setNumber(0, value)

    def getPlaceHolder(self):
        return self._getString(1)

    def setPlaceHolder(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(DialogTemplatePlaceHolderViewModel, self)._initialize()
        self._addNumberProperty('resourceID', 0)
        self._addStringProperty('placeHolder', '')