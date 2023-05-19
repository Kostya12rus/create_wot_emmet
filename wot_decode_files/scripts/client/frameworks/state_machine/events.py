# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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