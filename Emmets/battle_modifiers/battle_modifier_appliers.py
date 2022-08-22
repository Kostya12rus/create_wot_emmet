# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_modifiers/battle_modifier_appliers.py
from battle_modifier_constants import DataType, UseType, BattleParams
from battle_modifier_helpers import makeUseTypeMethods
from math_common import ceilTo
from constants import VEHICLE_HEALTH_DECIMALS
g_cache = {}
_defaultVal = lambda _, paramVal: paramVal
_defaultMul = lambda val, paramVal: val * paramVal
_defaultAdd = lambda val, paramVal: val + paramVal
_dataTypeAppliers = {DataType.INT: {UseType.VAL: _defaultVal, 
                  UseType.MUL: lambda val, paramVal: int(round(val * paramVal)), 
                  UseType.ADD: _defaultAdd}, 
   DataType.FLOAT: {UseType.VAL: _defaultVal, 
                    UseType.MUL: _defaultMul, 
                    UseType.ADD: _defaultAdd}}
_customAppliers = {BattleParams.VEHICLE_HEALTH: {UseType.MUL: lambda val, paramVal: int(ceilTo(val * paramVal, VEHICLE_HEALTH_DECIMALS))}}

def registerParamAppliers(paramId, dataType):
    global g_cache
    paramAppliers = makeUseTypeMethods(_dataTypeAppliers[dataType], True)
    if paramId in _customAppliers:
        paramAppliers.update(makeUseTypeMethods(_customAppliers[paramId]))
    g_cache[paramId] = paramAppliers