# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/cooldown.py
from constants import JOIN_FAILURE, REQUEST_COOLDOWN
from debug_utils import LOG_WARNING
from gui import SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as I18N_SYSTEM_MESSAGES
from gui.prb_control.formatters import messages
from gui.prb_control.settings import REQUEST_TYPE_NAMES, REQUEST_TYPE
from gui.shared import rq_cooldown as _rqc
from gui.shared.rq_cooldown import RequestCooldownManager, REQUEST_SCOPE
from helpers import i18n

def validatePrbCreationCooldown():
    if _rqc.isRequestInCoolDown(REQUEST_SCOPE.PRB_CONTROL, REQUEST_TYPE.CREATE):
        SystemMessages.pushMessage(messages.getJoinFailureMessage(JOIN_FAILURE.COOLDOWN), type=SystemMessages.SM_TYPE.Error)
        return True
    return False


def setPrbCreationCooldown():
    _rqc.setRequestCoolDown(REQUEST_SCOPE.PRB_CONTROL, REQUEST_TYPE.CREATE, coolDown=REQUEST_COOLDOWN.PREBATTLE_CREATION)


def getPrbRequestCoolDown(rqTypeID):
    return _rqc.getRequestCoolDown(REQUEST_SCOPE.PRB_CONTROL, rqTypeID)


class PrbCooldownManager(RequestCooldownManager):

    def __init__(self):
        super(PrbCooldownManager, self).__init__(REQUEST_SCOPE.PRB_CONTROL)

    def lookupName(self, rqTypeID):
        requestName = rqTypeID
        if rqTypeID in REQUEST_TYPE_NAMES:
            requestName = I18N_SYSTEM_MESSAGES.prebattle_request_name(REQUEST_TYPE_NAMES[rqTypeID])
            requestName = i18n.makeString(requestName)
        else:
            LOG_WARNING('Request type is not found', rqTypeID)
        return requestName

    def getDefaultCoolDown(self):
        return _rqc.DEFAULT_COOLDOWN_TO_REQUEST