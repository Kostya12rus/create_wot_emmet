# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/formatters.py
import math
from debug_utils import LOG_ERROR, LOG_WARNING

def normalizeHealth(health):
    return max(0.0, health)


def getHealthPercent(health, maxHealth):
    if not (maxHealth > 0 and maxHealth >= health):
        LOG_WARNING(('Maximum health is not valid! health={}, maxHealth={}').format(health, maxHealth))
        return 0.0
    return float(normalizeHealth(health)) / maxHealth


def normalizeHealthPercent(health, maxHealth):
    return int(math.ceil(getHealthPercent(health, maxHealth) * 100))


def formatHealthProgress(health, maxHealth):
    if not (maxHealth > 0 and maxHealth >= health):
        LOG_ERROR(('Maximum health is not valid! health={}, maxHealth={}').format(health, maxHealth))
    return '%d/%d' % (normalizeHealth(health), maxHealth)