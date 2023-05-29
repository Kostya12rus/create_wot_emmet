# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/__init__.py
from gui.battle_control.battle_session import BattleSessionProvider
from gui.battle_control.controllers import BattleSessionSetup
from skeletons.gui.battle_session import IBattleSessionProvider
__all__ = ('BattleSessionSetup', 'getBattleSessionConfig')

def getBattleSessionConfig(manager):
    manager.addInstance(IBattleSessionProvider, BattleSessionProvider(), finalizer='stop')