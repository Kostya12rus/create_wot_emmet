# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileSummaryPage.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSummary import ProfileSummary
from gui.Scaleform.locale.PROFILE import PROFILE

class ProfileSummaryPage(ProfileSummary):

    def __init__(self, *args):
        ProfileSummary.__init__(self, *args)

    def _getInitData(self):
        outcome = ProfileSummary._getInitData(self)
        outcome['nextAwardsLabel'] = PROFILE.SECTION_SUMMARY_LABELS_NEXTAWARDS
        outcome['nextAwardsErrorText'] = PROFILE.SECTION_SUMMARY_ERRORTEXT_NEXTAWARDS
        return outcome

    def getGlobalRating(self, userName):
        return self.itemsCache.items.stats.globalRating