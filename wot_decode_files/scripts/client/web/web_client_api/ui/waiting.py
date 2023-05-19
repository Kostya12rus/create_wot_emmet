# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/waiting.py
from gui.Scaleform.Waiting import Waiting
from web.web_client_api import w2c, W2CSchema, Field

class _WaitingToggleControlSchema(W2CSchema):
    enabled = Field(required=True, type=bool)


class _WaitingToggleSchema(W2CSchema):
    show = Field(required=True, type=bool)


class _GlobalWaitingToggleSchema(W2CSchema):
    show = Field(required=True, type=bool)
    messageID = Field(required=False, type=basestring, default='browser/w2c_call')


class WaitingWebApiMixin(object):

    @w2c(_WaitingToggleControlSchema, 'waiting_toggle_control')
    def waitingToggleControl(self, cmd, ctx):
        browserView = ctx['browser_view']
        browserView.browser.setAllowAutoLoadingScreen(not cmd.enabled)

    @w2c(_WaitingToggleSchema, 'waiting_toggle')
    def waitingToggle(self, cmd, ctx):
        browserView = ctx['browser_view']
        browserView.showLoading(cmd.show)

    @w2c(_GlobalWaitingToggleSchema, 'global_waiting_toggle')
    def globalWaitingToggle(self, cmd):
        if cmd.show:
            Waiting.show(cmd.messageID)
        else:
            Waiting.hide(cmd.messageID)