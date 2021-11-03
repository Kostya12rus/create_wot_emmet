# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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