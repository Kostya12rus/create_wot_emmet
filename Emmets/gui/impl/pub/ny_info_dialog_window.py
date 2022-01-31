# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/ny_info_dialog_window.py
from gui.impl.lobby.dialogs.contents.balance_content_with_ny_shards import BalanceContentWithShards
from gui.impl.pub.simple_dialog_window import SimpleDialogWindow

class NYInfoDialogWindow(SimpleDialogWindow):

    def __init__(self, *args, **kwargs):
        if kwargs.get('balanceContent') is not None:
            kwargs['balanceContent'] = BalanceContentWithShards()
        super(NYInfoDialogWindow, self).__init__(*args, **kwargs)
        return