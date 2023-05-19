# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/boosters.py
from web.web_client_api import w2c, W2CSchema, Field
from gui.shared import event_dispatcher as shared_events

class _OpenBoosterActivationWindow(W2CSchema):
    booster_id = Field(required=True, type=int)


class BoostersWindowWebApiMixin(object):

    @w2c(_OpenBoosterActivationWindow, 'booster_activation')
    def openBoosterActivationWindow(self, cmd):
        success = yield shared_events.showBoosterActivateDialog(cmd.booster_id)
        yield {'success': success}