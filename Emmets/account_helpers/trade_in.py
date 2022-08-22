# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/trade_in.py
import logging, time, typing, AccountCommands
if typing.TYPE_CHECKING:
    from Account import PlayerAccount
_logger = logging.getLogger(__name__)
_SECONDS_IN_DAY = 86400

class TradeIn(object):

    def __init__(self):
        self._account = None
        return

    def setAccount(self, account):
        self._account = account

    def addTokenDev(self, tokenID, expiryTimeOffset=_SECONDS_IN_DAY):
        currentTime = time.time()
        expiryTime = int(currentTime + expiryTimeOffset)
        self._account._doCmdIntStr(AccountCommands.CMD_TRADE_IN_ADD_TOKEN, expiryTime, tokenID, self._onCmdResponseReceived)

    def removeTokenDev(self, tokenID):
        self._account._doCmdStr(AccountCommands.CMD_TRADE_IN_REMOVE_TOKEN, tokenID, self._onCmdResponseReceived)

    def _onCmdResponseReceived(self, resultID, requestID, errorStr, errorMsg=None):
        if not AccountCommands.isCodeValid(requestID):
            _logger.error((errorStr, errorMsg))