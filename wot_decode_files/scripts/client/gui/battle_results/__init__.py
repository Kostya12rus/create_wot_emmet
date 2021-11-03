# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/__init__.py
from gui.battle_results.service import BattleResultsService
from gui.battle_results.context import RequestResultsContext
from gui.battle_results.context import RequestEmblemContext
from gui.battle_results.settings import EMBLEM_TYPE
from skeletons.gui.battle_results import IBattleResultsService
__all__ = ('getBattleResultsServiceConfig', 'RequestResultsContext', 'RequestEmblemContext',
           'EMBLEM_TYPE')

def getBattleResultsServiceConfig(manager):
    instance = BattleResultsService()
    instance.init()
    manager.addInstance(IBattleResultsService, instance, finalizer='fini')