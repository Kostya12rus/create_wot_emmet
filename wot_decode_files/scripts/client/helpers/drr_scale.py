# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/drr_scale.py
import BigWorld
DRR_MIN_SCALE_VALUE = 0.6
DRR_MAX_SCALE_VALUE = 1.0
DRR_MAX_STEP_VALUE = 0.05
DRR_EPSILON_VALUE = DRR_MAX_STEP_VALUE - 0.01
PERCENT_MODIFIER = 100.0

def normalizeScale(value):
    result = min(max(round(value, 2), DRR_MIN_SCALE_VALUE), DRR_MAX_SCALE_VALUE)
    modulo = result * PERCENT_MODIFIER % (DRR_MAX_STEP_VALUE * PERCENT_MODIFIER)
    if modulo:
        result = result - modulo / PERCENT_MODIFIER
    return result


def getPercent(value):
    return round(value, 3) * PERCENT_MODIFIER


def changeScaleByStep(offset):
    result = None
    scale = BigWorld.getDRRScale()
    newScale = normalizeScale(scale + offset)
    if abs(scale - newScale) >= DRR_EPSILON_VALUE:
        BigWorld.setDRRScale(newScale)
        if normalizeScale(BigWorld.getDRRScale()) == newScale:
            result = newScale
    return result


def stepUp():
    return changeScaleByStep(DRR_MAX_STEP_VALUE)


def stepDown():
    return changeScaleByStep(-DRR_MAX_STEP_VALUE)