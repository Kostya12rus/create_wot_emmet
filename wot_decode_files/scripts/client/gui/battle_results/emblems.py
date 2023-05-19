# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/emblems.py
from adisp import adisp_process
from gui.battle_results.settings import EMBLEM_TYPE
from gui.shared.ClanCache import g_clanCache

class EmblemFetcher(object):
    __slots__ = ('_formationDBID', '_url', '_callback')

    def __init__(self, formationDBID):
        super(EmblemFetcher, self).__init__()
        self._formationDBID = formationDBID
        self._url = ''
        self._callback = None
        return

    def clear(self):
        self._callback = None
        return

    def fetch(self, callback):
        callback(None)
        return

    def getURL(self):
        return self._url


class ClanEmblemFetcher(EmblemFetcher):
    __slots__ = ('_url', )

    def __init__(self, formationDBID, textureID):
        super(ClanEmblemFetcher, self).__init__(formationDBID)
        self._url = textureID

    @adisp_process
    def fetch(self, callback):
        self._url = yield g_clanCache.getClanEmblemTextureID(self._formationDBID, False, self._url)
        callback(self._url)


def createFetcher(ctx):
    emblemType = ctx.getEmblemType()
    fetcher = None
    if emblemType == EMBLEM_TYPE.CLAN:
        fetcher = ClanEmblemFetcher(ctx.getFormationDBID(), ctx.getTextureID())
    return fetcher