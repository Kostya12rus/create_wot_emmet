# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/tankman.py
from gui.server_events.recruit_helper import getRecruitInfo
from web.web_client_api import w2c, W2CSchema, Field
from gui.server_events import events_dispatcher as server_events

class _RecruitIDSchema(W2CSchema):
    recruit_id = Field(required=True, type=basestring, validator=(lambda value, _: _tankManTokenValidator(value)))


def _tankManTokenValidator(tokenID):
    return getRecruitInfo(tokenID) is not None


class OpenTankmanWebApiMixin(object):

    @w2c(_RecruitIDSchema, 'recruit')
    def openRecruitingWindow(self, cmd):
        server_events.showRecruitWindow(cmd.recruit_id.encode())