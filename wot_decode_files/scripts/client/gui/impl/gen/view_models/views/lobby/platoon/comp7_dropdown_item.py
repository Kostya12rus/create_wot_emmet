# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/comp7_dropdown_item.py
from gui.impl.gen.view_models.ui_kit.gf_drop_down_item import GfDropDownItem
from gui.impl.gen.view_models.views.lobby.platoon.comp7_dropdown_item_meta import Comp7DropdownItemMeta

class Comp7DropdownItem(GfDropDownItem):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(Comp7DropdownItem, self).__init__(properties=properties, commands=commands)

    @property
    def meta(self):
        return self._getViewModel(3)

    @staticmethod
    def getMetaType():
        return Comp7DropdownItemMeta

    def _initialize(self):
        super(Comp7DropdownItem, self)._initialize()
        self._addViewModelProperty('meta', Comp7DropdownItemMeta())