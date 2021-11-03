# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/battle_royale/__init__.py
from CurrentVehicle import g_currentPreviewVehicle
from gui.prb_control.settings import FUNCTIONAL_FLAG

def isNeedToLoadHangar(ctx):
    if g_currentPreviewVehicle.isPresent():
        reqFlags = FUNCTIONAL_FLAG.LOAD_PAGE | FUNCTIONAL_FLAG.SWITCH | FUNCTIONAL_FLAG.TRAINING
        if ctx and not ctx.hasFlags(reqFlags):
            return True
    return False