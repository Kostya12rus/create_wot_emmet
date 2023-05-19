# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/custom_actions_keeper.py


class CustomActionsKeeper(object):
    __actions = {}

    @classmethod
    def registerAction(cls, actionId, actionHandler):
        cls.__actions[actionId] = actionHandler

    @classmethod
    def getAction(cls, actionId):
        return cls.__actions.get(actionId, None)

    @classmethod
    def invoke(cls, actor, **kwargs):
        if actor is None:
            return
        else:
            if hasattr(actor, 'invoke'):
                actor.invoke(**kwargs)
            else:
                actor(**kwargs)
            return