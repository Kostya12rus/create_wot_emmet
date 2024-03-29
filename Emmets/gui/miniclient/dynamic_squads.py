# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/dynamic_squads.py
from account_helpers.settings_core.settings_constants import GAME
from gui.battle_control.arena_info.settings import PERSONAL_STATUS
from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class ParametrizeInitPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.battle_control.battle_ctx', 'BattleContext', 'isInvitationEnabled', aspects=(
         _ParametrizeInitAspect,))


class _RemoveShowInvitesFlagAspect(aop.Aspect):

    def atCall(self, cd):
        status = cd.findArg(0, 'bitmask')
        if status & PERSONAL_STATUS.SHOW_ALLY_INVITES > 0:
            status ^= PERSONAL_STATUS.SHOW_ALLY_INVITES
            return cd.changeArgs((0, 'bitmask', status))
        else:
            return


class RemoveShowInvitesFlagPointcut(aop.Pointcut):

    def __init__(self):
        super(RemoveShowInvitesFlagPointcut, self).__init__('gui.Scaleform.daapi.view.battle.shared.stats_exchange', 'BattleStatisticsDataController', 'as_setPersonalStatusS', aspects=(
         _RemoveShowInvitesFlagAspect(),))


class _DisableGameSettingAspect(aop.Aspect):

    def atCall(self, cd):
        if cd.self.settingName == GAME.RECEIVE_INVITES_IN_BATTLE:
            cd.avoid()
        return


class DisableGameSettingPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'account_helpers.settings_core.options', 'MessengerSetting', '_get', aspects=(
         _DisableGameSettingAspect,))


class InviteReceivedMessagePointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.battle_control.controllers.dyn_squad_functional', 'DynSquadMessagesController', '_inviteReceived', aspects=(
         aop.DummyAspect,))