# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/auto_shoot_guns/auto_shoot_wrappers.py
from functools import wraps
import operator

def autoCooldown(method):

    @wraps(method)
    def wrapper(burstPredictor, *args, **kwargs):
        if burstPredictor.isShootingPossible():
            return method(burstPredictor, *args, **kwargs)
        burstPredictor.activateCooldown()

    return wrapper


def checkPredictionStates(states=(), defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(burstPredictor, *args, **kwargs):
            if burstPredictor.getPredictionState() in states:
                return method(burstPredictor, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(burstPredictor)
                return defReturn

        return wrapper

    return decorator


def checkStateStatus(states=(), defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(controller, *args, **kwargs):
            stateStatus = controller.stateStatus
            if stateStatus is not None and stateStatus.state in states:
                return method(controller, stateStatus, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(controller)
                return defReturn

        return wrapper

    return decorator