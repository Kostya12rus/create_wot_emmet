# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/dialogs.py
import adisp, wg_async
from gui.impl.pub.dialog_window import DialogButtons
from gui.shared.event_dispatcher import showPreformattedDialog
from shared_utils import first
from web.web_client_api import WebCommandException, w2c, W2CSchema, Field

def _dialogButtonsValidator(buttonsList, _=None):
    for button in buttonsList:
        if first(button.keys()) not in DialogButtons.ALL:
            raise WebCommandException(('unsupported button label "{}"').format(first(button.keys())))

    return True


class _DialogSchema(W2CSchema):
    preset = Field(required=True, type=basestring)
    title = Field(required=False, type=basestring, default='')
    message = Field(required=False, type=basestring, default='')
    buttons = Field(required=True, type=list, validator=_dialogButtonsValidator)
    focusedButton = Field(required=False, type=basestring, default=None)
    btnDownSounds = Field(required=False, type=dict, default=None)


class DialogsWebApiMixin(object):

    @w2c(_DialogSchema, 'confirm_dialog_overlay')
    def showDialog(self, cmd):

        @adisp.adisp_async
        @wg_async.wg_async
        def proxy(callback):
            res = yield wg_async.wg_await(showPreformattedDialog(cmd.preset, cmd.title, cmd.message, cmd.buttons, cmd.focusedButton, cmd.btnDownSounds))
            callback(res)

        result = yield proxy()
        yield {'buttonID': result}