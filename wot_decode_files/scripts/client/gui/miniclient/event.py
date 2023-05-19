# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/event.py
from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class _DisableEventBoards(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitEventPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.event_battles_controller', 'EventBattlesController', 'isEnabled', aspects=(
         _ParametrizeInitAspect,))


class DisableEventBoards(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'helpers.server_settings', 'ServerSettings', 'isElenEnabled', aspects=(
         _DisableEventBoards,))