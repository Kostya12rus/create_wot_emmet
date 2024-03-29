# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/__init__.py
import PlayerEvents
from gui.shared.system_factory import collectBattleControllerRepo
from gui.battle_control.controllers.repositories import BattleSessionSetup
from gui.battle_control.controllers.repositories import SharedControllersLocator
from gui.battle_control.controllers.repositories import DynamicControllersLocator
from gui.battle_control.controllers.repositories import ClassicControllersRepository
from gui.battle_control.controllers.repositories import SharedControllersRepository
from gui.battle_control.controllers.repositories import _ControllersRepository
__all__ = ('createShared', 'createDynamic', 'BattleSessionSetup', 'SharedControllersLocator',
           'DynamicControllersLocator', '_ControllersRepository')

def createShared(setup):
    return SharedControllersLocator(SharedControllersRepository.create(setup))


def createDynamic(setup):
    repository, inited = collectBattleControllerRepo(setup.arenaVisitor.gui.guiType, setup)
    if not inited:
        repository = ClassicControllersRepository.create(setup)
    return DynamicControllersLocator(repository=repository)