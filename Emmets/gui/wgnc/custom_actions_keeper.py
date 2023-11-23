# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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