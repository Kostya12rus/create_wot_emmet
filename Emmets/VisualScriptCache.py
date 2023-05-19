# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/VisualScriptCache.py
import BigWorld
from visual_script.misc import ASPECT
from visual_script.multi_plan_provider import MultiPlanCache

class VisualScriptCache(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(VisualScriptCache, self).__init__()
        self._multiPlanCache = MultiPlanCache(ASPECT.CLIENT)

    def onDestroy(self):
        self._multiPlanCache.destroy()

    def getPlan(self, componentName, planNames):
        return self._multiPlanCache.getPlan(componentName, planNames)