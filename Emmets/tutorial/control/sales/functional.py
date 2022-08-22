# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/sales/functional.py
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared import g_eventBus, events
from tutorial.control.functional import FunctionalEffect

class LoadViewEffect(FunctionalEffect):

    def __init__(self, effect):
        self._isRunning = False
        super(LoadViewEffect, self).__init__(effect)

    def triggerEffect(self):
        viewData = self.getTarget()
        if viewData is not None:
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(viewData.getAlias()), ctx=viewData.getCtx()), scope=viewData.getScope())
            return True
        else:
            return False