# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/tank_carousel/__init__.py
import pointcuts as _pointcuts

def configure_pointcuts(config):
    _pointcuts.MakeTankUnavailableInCarousel(config)
    _pointcuts.VehicleTooltipStatus(config)