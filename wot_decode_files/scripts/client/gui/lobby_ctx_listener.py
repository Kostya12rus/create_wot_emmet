# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lobby_ctx_listener.py
_CHANGE_NOTIFIERS = []

def _getValueFromPath(path, data):
    if not path:
        return data
    else:
        if path[0] in data:
            return _getValueFromPath(path[1:], data[path[0]])
        return


class LobbyContextChangeListener(object):
    __slots__ = ('__notifiers', '__proxy')

    def __init__(self, proxy):
        self.__notifiers = []
        self.__proxy = proxy
        for notifier in _CHANGE_NOTIFIERS:
            self.addNotifier(notifier)

    def addNotifier(self, notifier):
        self.__notifiers.append(notifier)

    def update(self, data):
        for notifier in self.__notifiers:
            path = notifier.getPath()
            currentValue = _getValueFromPath(path, self.__proxy.getServerSettings().getSettings())
            nextValue = _getValueFromPath(path, data)
            if nextValue is not None:
                notifier(nextValue, currentValue)

        return