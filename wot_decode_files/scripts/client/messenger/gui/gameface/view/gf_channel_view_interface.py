# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/gameface/view/gf_channel_view_interface.py


class GFChannelViewInterface(object):

    def onChannelControllerInited(self, channelCtrl):
        pass

    def addMessageToView(self, message, isHistoryMessage=False):
        return False