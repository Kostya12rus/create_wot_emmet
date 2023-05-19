# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/base.py
from collections import namedtuple
import logging
from pprint import pformat
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
_logger = logging.getLogger(__name__)

def _defaultLogger(*args):
    msg = pformat(args)
    _logger.debug('[SERVER CMD RESPONSE]:%s', msg)


def _getProxy(callback):
    if callback is not None:
        return (lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext))
    else:
        return


FestivityQuestsHangarFlag = namedtuple('FestivityQuestsHangarFlag', 'icon, iconDisabled, flagBackground')

class BaseFestivityRequester(AbstractSyncDataRequester):
    dataKey = None

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().festivities.getCache((lambda resID, value: self._response(resID, value, callback)))

    def _preprocessValidData(self, data):
        festivityData = data.get(self.dataKey, {})
        return dict(festivityData)


class BaseFestivityProcessor(object):

    def __init__(self):
        super(BaseFestivityProcessor, self).__init__()
        self.__commandProxy = None
        return

    def setCommandProxy(self, account):
        self.__commandProxy = account

    def _perform(self, command, callback=None, *args):
        cmdArgs = list(args) + [_getProxy(callback)]
        self.__commandProxy.perform(command, *cmdArgs)