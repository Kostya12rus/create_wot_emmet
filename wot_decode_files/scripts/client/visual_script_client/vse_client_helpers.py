# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/vse_client_helpers.py
import BigWorld

def runPlan(entity, planName, params, key='', contextName=''):
    player = BigWorld.player()
    if player is not None:
        arena = player.arena
        if arena is not None:
            context = None
            if contextName:
                if entity and hasattr(entity, 'getVseContextInstance'):
                    context = entity.getVseContextInstance(contextName)
                else:
                    context = arena.getVseContextInstance(contextName)
            arena.runVsePlan(planName, params, key, context)
    return


def stopPlan(planName, key=''):
    player = BigWorld.player()
    if player is not None:
        arena = player.arena
        if arena is not None:
            arena.stopVsePlan(planName, key)
    return