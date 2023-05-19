# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/referral.py
from gui.Scaleform.daapi.view.lobby.referral_program.referral_program_helpers import isReferralProgramEnabled
from helpers import dependency
from skeletons.gui.game_control import IReferralProgramController
from web.web_client_api import w2c, W2CSchema

class ReferralProgramPagesMixin(object):
    __referralCtrl = dependency.descriptor(IReferralProgramController)

    @w2c(W2CSchema, 'referral_program_view')
    def openReferralProgramView(self, _):
        if self.__referralCtrl and isReferralProgramEnabled():
            self.__referralCtrl.showWindow()
        return {'success': self.__referralCtrl and isReferralProgramEnabled()}