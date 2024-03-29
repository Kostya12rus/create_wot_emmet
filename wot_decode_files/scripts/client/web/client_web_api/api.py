# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/api.py
import json, time, weakref, typing
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, Optional, Tuple, Union
    from web.client_web_api.common import WebEventSender
    WebEvent = Dict[(str, Union[(float, str, Dict[(Ellipsis, Ellipsis)])])]
    HashedEvent = Tuple[(int, int, int)]
_TYPE = 'type'
_DATA = 'data'
_TIME = 'time'

class C2WHandler(object):

    def __init__(self, sender):
        super(C2WHandler, self).__init__()
        self.__sender = weakref.proxy(sender)
        self.__previous = {}

    @property
    def preventIdentical(self):
        return True

    def init(self):
        pass

    def fini(self):
        self.__sender = None
        return

    def _sendWebEvent(self, webEvent):
        if self.__sender is not None:
            hashedEvent = self.__hashedEvent(webEvent)
            if self.preventIdentical and self.__isDuplicate(*hashedEvent):
                return
            try:
                del webEvent[_TIME]
                self.__sender.sendEvent(json.dumps(webEvent))
                self.__cachePrevious(*hashedEvent)
            except ReferenceError:
                return

        return

    def __isDuplicate(self, eTime, eType, eData):
        return self.__previous.get(eType) == (eTime, eData)

    def __cachePrevious(self, eTime, eType, eData):
        self.__previous[eType] = (
         eTime, eData)

    @staticmethod
    def __hashedEvent(webEvent):
        return (
         hash(json.dumps(webEvent[_TIME])),
         hash(json.dumps(webEvent[_TYPE])),
         hash(json.dumps(webEvent[_DATA], ensure_ascii=False)))


def c2w(name, preventIdentical=True):

    def decorator(method):

        def wrapped(self, *args, **kwargs):
            self._sendWebEvent({_TIME: time.time() if preventIdentical else 0.0, 
               _TYPE: name, 
               _DATA: method(self, *args, **kwargs) or {}})

        return wrapped

    return decorator