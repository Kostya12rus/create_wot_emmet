# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/fun_random/pre_queue/scheduler.py
from gui.impl.gen import R
from gui.periodic_battles.prb_control.scheduler import PeriodicScheduler
from helpers import dependency
from skeletons.gui.game_control import IFunRandomController

class FunRandomScheduler(PeriodicScheduler):
    _RES_ROOT = R.strings.system_messages.funRandom
    _controller = dependency.descriptor(IFunRandomController)