# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/referral_program_requester.py
import BigWorld
from adisp import adisp_async
from account_helpers.referral_program import RP_PDATA_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IReferralProgramRequester

class ReferralProgramRequester(AbstractSyncDataRequester, IReferralProgramRequester):

    def getRPPgbPoints(self):
        return self.getCacheValue('pgbPoints')

    def getRPExpirationTime(self):
        return self.getCacheValue('expirationTime')

    def getRecruitDelta(self):
        return self.getCacheValue('recruitDelta')

    def getRPPassiveIncome(self):
        return self.getCacheValue('passiveIncome', defaultValue=0)

    def _preprocessValidData(self, data):
        return dict(data.get(RP_PDATA_KEY, {}))

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().referralProgram.getCache((lambda resID, value: self._response(resID, value, callback)))