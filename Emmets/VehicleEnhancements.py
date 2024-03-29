# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/VehicleEnhancements.py
from items.vehicles import EnhancementItem

class VehicleEnhancements(object):

    def __init__(self, enhancements):
        self.factors = []
        for items in enhancements.itervalues():
            for enhancement in items.itervalues():
                if 'factors' in enhancement:
                    self.factors.extend([ EnhancementItem(factor['name'], factor['value'], factor['operation']) for factor in enhancement['factors']
                                        ])

    def onCollectFactors(self, factors):
        for factor in self.factors:
            factors[factor.name] = factor.applyFactor(factors[factor.name])