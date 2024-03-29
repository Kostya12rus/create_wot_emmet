# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/header/battle_selector_extra_item.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.header.battle_selector_item import SelectorItem

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