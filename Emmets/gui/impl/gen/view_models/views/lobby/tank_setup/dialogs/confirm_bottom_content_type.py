# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/confirm_bottom_content_type.py
from gui.impl.gen.view_models.views.lobby.common.buy_and_exchange_bottom_content_type import BuyAndExchangeBottomContentType

class ConfirmBottomContentType(BuyAndExchangeBottomContentType):
    __slots__ = ()
    SAVE_SLOTS_CONTENT = 'saveSlotsContent'

    def __init__(self, properties=0, commands=0):
        super(ConfirmBottomContentType, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ConfirmBottomContentType, self)._initialize()