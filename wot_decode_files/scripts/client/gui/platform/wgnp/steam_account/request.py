# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/steam_account/request.py
from constants import WG_GAMES
from gui.platform.base.request import Params
from gui.platform.wgnp.steam_account.response import WGNPSteamAccEmailAddResponse, WGNPSteamAccEmailConfirmResponse

class EmailStatusParams(Params):
    url = './personal/api/v2/account/email/state/'
    headers = {'Content-Type': 'application/json'}
    method = 'POST'


class AddEmailParams(Params):
    response = WGNPSteamAccEmailAddResponse
    url = './personal/api/v2/account/email/create/'
    headers = {'Content-Type': 'application/json'}
    proofOfWorkURL = './personal/api/v2/account/email/create/challenge/?type=pow'
    method = 'POST'
    queryParams = {'type': 'pow'}
    postData = {'game': WG_GAMES.TANKS}

    def __init__(self, urlHost, email):
        super(AddEmailParams, self).__init__(urlHost)
        self.postData['email'] = email


class ConfirmEmailParams(Params):
    response = WGNPSteamAccEmailConfirmResponse
    url = './personal/api/v2/account/email/activate/'
    headers = {'Content-Type': 'application/json'}
    method = 'POST'

    def __init__(self, urlHost, code):
        super(ConfirmEmailParams, self).__init__(urlHost)
        self.postData['code'] = code