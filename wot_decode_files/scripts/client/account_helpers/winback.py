# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/winback.py
import typing, AccountCommands
if typing.TYPE_CHECKING:
    from typing import Callable, Optional

class Winback(object):

    def __init__(self, commandsProxy):
        self.__commandsProxy = commandsProxy

    def turnOffBattles(self, reason, callback):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr)
        else:
            proxy = None
        self.__commandsProxy.perform(AccountCommands.CMD_TURNOFF_WINBACK_BATTLES, reason, proxy)
        return