# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/SimpleStreamResponseHandler.py
import weakref, zlib, cPickle, AccountCommands
from debug_utils import LOG_CODEPOINT_WARNING, LOG_CURRENT_EXCEPTION

class SimpleStreamResponseHandler(object):

    def __init__(self, account, callback, default=None):
        self.__accountRef = weakref.ref(account)
        self.__callback = callback
        self.__default = default

    def __call__(self, requestID, resultID, errorStr, ext=None):
        ext = ext or {}
        if resultID != AccountCommands.RES_STREAM:
            self.__callback(resultID, self.__default)
        else:
            self.__accountRef()._subscribeForStream(requestID, self.__onStreamComplete)

    def __onStreamComplete(self, isSuccess, data):
        if isSuccess:
            if data is None:
                LOG_CODEPOINT_WARNING()
                isSuccess = False
            else:
                try:
                    data = zlib.decompress(data)
                    data = cPickle.loads(data)
                except Exception:
                    LOG_CURRENT_EXCEPTION()
                    isSuccess = False

        if isSuccess:
            self.__callback(AccountCommands.RES_STREAM, data)
        else:
            self.__callback(AccountCommands.RES_FAILURE, self.__default)
        return