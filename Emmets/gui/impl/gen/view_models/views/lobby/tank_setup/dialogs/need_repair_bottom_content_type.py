# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/need_repair_bottom_content_type.py
from gui.impl.gen.view_models.views.lobby.common.buy_and_exchange_bottom_content_type import BuyAndExchangeBottomContentType

class NeedRepairBottomContentType(BuyAndExchangeBottomContentType):
    __slots__ = ()
    NOT_NEED_REPAIR = 'notNeedRepair'

    def __init__(self, properties=0, commands=0):
        super(NeedRepairBottomContentType, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(NeedRepairBottomContentType, self)._initialize()