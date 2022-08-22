# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/invitations/aspects.py
from gui import makeHtmlString
from helpers import aop
from helpers.i18n import makeString as _ms
from constants import PREBATTLE_TYPE_NAMES
from notification.settings import NOTIFICATION_BUTTON_STATE

class DisableAccept(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InvitationNote(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        battle_type = PREBATTLE_TYPE_NAMES[cd.args[0].type]
        return makeHtmlString('html_templates:lobby/prebattle', 'inviteNote', {'note': _ms(('#miniclient:invitation/note/{0}').format(battle_type))})


class DisableAcceptButton(aop.Aspect):

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_buttons = original_return_value['message']['buttonsStates']
        original_buttons['submit'] = original_buttons['submit'] & ~NOTIFICATION_BUTTON_STATE.ENABLED
        return original_return_value