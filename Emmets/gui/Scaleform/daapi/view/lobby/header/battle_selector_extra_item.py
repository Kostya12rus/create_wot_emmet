# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/header/battle_selector_extra_item.py
from battle_selector_item import SelectorItem

class SelectorExtraItem(SelectorItem):

    def __init__(self, label, data, order, selectorType=None, isVisible=True):
        super(SelectorExtraItem, self).__init__(label, data, order, selectorType, isVisible, isExtra=True)

    def getVO(self):
        vo = super(SelectorExtraItem, self).getVO()
        vo.update({'mainLabel': self.getMainLabel(), 
           'infoLabel': self.getInfoLabel(), 
           'ribbonSrc': self.getRibbonSrc()})
        return vo

    def getMainLabel(self):
        raise NotImplementedError

    def getInfoLabel(self):
        raise NotImplementedError

    def getRibbonSrc(self):
        raise NotImplementedError

    def _update(self, state):
        raise NotImplementedError