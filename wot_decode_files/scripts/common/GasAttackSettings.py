# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/GasAttackSettings.py
import Math

class GasAttackState(object):
    NO = 0
    PREPARE = 1
    ATTACK = 2
    DONE = 3


class GasAttackSettings:
    DEATH_DELAY = 10

    def __init__(self, attackLength, preparationPeriod, position, startRadius, endRadius, compressionTime):
        self.attackLength = attackLength
        self.preparationPeriod = preparationPeriod
        self.position = Math.Vector3(position)
        self.startRadius = startRadius
        self.endRadius = endRadius
        self.compressionTime = compressionTime
        if compressionTime == 0:
            self.compressionSpeed = 0
            self.startRadius = self.endRadius
        else:
            self.compressionSpeed = float(startRadius - endRadius) / compressionTime


def gasAttackStateFor(settings, timeFromActivation):
    if timeFromActivation <= settings.preparationPeriod:
        return (GasAttackState.PREPARE, (settings.position, settings.startRadius))
    currentRadius = settings.startRadius - (timeFromActivation - settings.preparationPeriod) * settings.compressionSpeed
    if currentRadius <= settings.endRadius:
        return (GasAttackState.DONE, (settings.position, settings.endRadius))
    return (GasAttackState.ATTACK, (settings.position, currentRadius))