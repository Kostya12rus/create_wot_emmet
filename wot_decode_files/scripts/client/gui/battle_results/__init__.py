# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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