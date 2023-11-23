# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/user_cm_handlers.py
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import USER
from helpers import aop

class UserCmClanUnavailableAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        for item in original_return_options:
            if item['id'] == USER.CLAN_INFO:
                if not item['initData']:
                    item['initData'] = {}
                item['initData']['enabled'] = False
                break

        return original_return_options


class UserCmInviteClanUnavailableAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        for item in original_return_options:
            if item['id'] == USER.SEND_CLAN_INVITE:
                if not item['initData']:
                    item['initData'] = {}
                item['initData']['enabled'] = False
                break

        return original_return_options


class UserCmClanUnavailablePointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.user_cm_handlers', 'BaseUserCMHandler', '_addClanProfileInfo', aspects=(
         UserCmClanUnavailableAspect,))


class UserCmInviteClanUnavailablePointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.user_cm_handlers', 'BaseUserCMHandler', '_addInviteClanInfo', aspects=(
         UserCmInviteClanUnavailableAspect,))