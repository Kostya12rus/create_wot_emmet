# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehModulesConfiguratorCmpMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehModulesConfiguratorCmpMeta(BaseDAAPIComponent):

    def onClick(self, intCD, columnIdx, moduleIdx):
        self._printOverrideError('onClick')

    def as_setItemsS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(items)

    def as_updateItemsS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_updateItems(items)