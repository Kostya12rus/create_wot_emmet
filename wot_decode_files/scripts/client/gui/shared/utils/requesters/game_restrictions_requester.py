# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/game_restrictions_requester.py
import typing, BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGameRestrictionsRequester

class GameRestrictionsRequester(AbstractSyncDataRequester, IGameRestrictionsRequester):

    @property
    def session(self):
        return self.getCacheValue('session', {})

    @property
    def hasSessionLimit(self):
        return len(self.session) > 0

    def getKickAt(self):
        return self.getCacheValue('session', {}).get('kick_at', 0)

    @property
    def settings(self):
        return self.getCacheValue('settings', {})

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().gameRestrictions.getCache((lambda resID, value: self._response(resID, value, callback)))