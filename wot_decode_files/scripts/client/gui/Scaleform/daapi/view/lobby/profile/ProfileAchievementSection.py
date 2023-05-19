# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileAchievementSection.py
from gui.Scaleform.daapi.view.meta.ProfileAchievementSectionMeta import ProfileAchievementSectionMeta
from helpers import dependency
from skeletons.gui.shared.utils import IRaresCache

class ProfileAchievementSection(ProfileAchievementSectionMeta):
    rareAchievesCache = dependency.descriptor(IRaresCache)

    def __init__(self, *args):
        super(ProfileAchievementSection, self).__init__(*args)
        self.rareAchievesCache.onImageReceived += self._onRareImageReceived

    def _onRareImageReceived(self, imgType, rareID, imageData):
        pass

    def _disposeRequester(self):
        self.rareAchievesCache.onImageReceived -= self._onRareImageReceived