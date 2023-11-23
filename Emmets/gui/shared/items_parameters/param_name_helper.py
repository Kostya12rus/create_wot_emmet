# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/items_parameters/param_name_helper.py
import logging
from gui.impl.gen import R
_logger = logging.getLogger(__name__)

def getVehicleParameterText(paramName, isTTC=False, isLong=False, isPositive=False):
    res = default = R.strings.tank_setup.kpi.bonus
    if isTTC:
        res = res.ttc
    else:
        if isLong:
            res = res.longDescr
        if isPositive:
            res = res.positive
            default = default.positive
        else:
            res = res.negative
            default = default.negative
        result = res.dyn(paramName) or default.dyn(paramName)
        if not result:
            _logger.debug('Text for vehicle parameter is not found: name=%s, isTTC=%s, isLong=%s, isPositive=%s', paramName, isTTC, isLong, isPositive)
            return R.invalid()
    return result()