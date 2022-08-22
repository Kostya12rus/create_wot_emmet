# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/shop.py
from helpers import aop
from helpers.i18n import makeString as _ms
from gui.shared.gui_items import GUI_ITEM_TYPE

class _OnShopItemWrapAspect(aop.Aspect):

    def __init__(self, config):
        self.__config = config
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        original_wrapping = cd.returned
        packedItem = cd.args[0]
        module = packedItem[0]
        warnMessage = ''
        if module.itemTypeID == GUI_ITEM_TYPE.VEHICLE and not self.__config['vehicle_is_available'](module):
            warnMessage = _ms('#miniclient:shop_vehicle_item_renderer/warn_message')
        original_wrapping['warnMessage'] = warnMessage
        return original_wrapping


class OnShopItemWrapPointcut(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.store.tabs.shop', 'ShopVehicleTab', 'itemWrapper', aspects=(
         _OnShopItemWrapAspect(config),))