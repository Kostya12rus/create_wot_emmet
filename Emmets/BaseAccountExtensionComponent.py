# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/BaseAccountExtensionComponent.py
import BigWorld
from helpers import isPlayerAccount

class BaseAccountExtensionComponent(BigWorld.StaticScriptComponent):

    @property
    def account(self):
        return self.entity

    @property
    def base(self):
        return self.account.base

    @classmethod
    def instance(cls):
        playerAccount = BigWorld.player()
        if isPlayerAccount() and cls.__name__ in playerAccount.components:
            return getattr(playerAccount, cls.__name__, None)
        else:
            return