# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/game_restrictions_requester.py
import typing, BigWorld
from adisp import async
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

    @async
    def _requestCache(self, callback):
        BigWorld.player().gameRestrictions.getCache(lambda resID, value: self._response(resID, value, callback))