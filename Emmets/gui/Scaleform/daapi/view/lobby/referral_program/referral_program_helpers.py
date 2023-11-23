# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/referral_program/referral_program_helpers.py
from gui import GUI_SETTINGS
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
REF_RPOGRAM_PDATA_KEY = 'refProgram'
RECRUITER_ID_ATTR = 'recruiterId'

def _getUrl(urlName=None):
    if urlName is None:
        return getReferralProgramURL()
    else:
        return getReferralProgramURL() + GUI_SETTINGS.referralProgram.get(urlName)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def isReferralProgramEnabled(lobbyContext=None):
    return lobbyContext and lobbyContext.getServerSettings().isReferralProgramEnabled()


def getReferralProgramURL():
    return GUI_SETTINGS.referralProgram.get('baseUrl')


def getObtainVehicleURL():
    return _getUrl('getVehicle')


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def isCurrentUserRecruit(itemsCache=None):
    return bool(itemsCache.items.stats.refSystem20.get(RECRUITER_ID_ATTR, False))