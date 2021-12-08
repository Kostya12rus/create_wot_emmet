# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/state_machine/events.py


class StateEvent(object):
    __slots__ = ('__arguments', )

    def __init__(self, *args, **kwargs):
        super(StateEvent, self).__init__()
        self.__arguments = kwargs

    def __repr__(self):
        return ('{}({})').format(self.__class__.__name__, id(self))

    def getArgument(self, name, default=None):
        return self.__arguments.get(name, default)

    def getArguments(self):
        return self.__arguments


class StringEvent(StateEvent):
    __slots__ = ('__token', )

    def __init__(self, token, **kwargs):
        super(StringEvent, self).__init__(**kwargs)
        self.__token = token

    def __repr__(self):
        return ('{}({})').format(self.__class__.__name__, self.__token)

    @property
    def token(self):
        return self.__token