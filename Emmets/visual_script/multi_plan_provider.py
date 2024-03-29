# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/multi_plan_provider.py
import VSE
from context import VScriptContext
from typing import Iterable, Any
from plan_tags import PlanTags
from constants import IS_DEVELOPMENT
from soft_exception import SoftException
from plan_holder import PlanHolder

class MultiPlanProvider(object):

    def __init__(self, aspect, arenaBonusType=0):
        self._plans = {}
        self._aspect = aspect
        self._context = None
        self._planTags = PlanTags(arenaBonusType)
        return

    def destroy(self):
        pass

    def reset(self):
        self.stop()
        for holder in self._plans.itervalues():
            holder.loadState = PlanHolder.INACTIVE

        self._plans = {}
        self._context = None
        return

    def get(self, planName):
        return self._plans.get(planName, PlanHolder(None, PlanHolder.INACTIVE)).plan

    def start(self):
        for holder in self._plans.itervalues():
            holder.setOptionalInputParams(**holder.params)
            if holder.isLoaded:
                holder.plan.start(holder.params)
            holder.autoStart = True

    def stop(self):
        for holder in self._plans.itervalues():
            if holder.isLoaded:
                holder.plan.stop()
            holder.autoStart = False

    def restart(self):
        for holder in self._plans.itervalues():
            holder.setOptionalInputParams(**holder.params)
            if holder.isLoaded:
                holder.plan.stop()
                holder.plan.start(holder.params)

    def pause(self):
        map((lambda holder: holder.plan.pause() if holder.isLoaded else None), self._plans.itervalues())

    def isLoaded(self):
        return all(holder.isLoaded or holder.isLoadCanceled for holder in self._plans.itervalues())

    def isError(self):
        return any(holder.isError for holder in self._plans.itervalues())

    def load(self, planNames, autoStart=False):
        self.reset()
        for entry in planNames:
            if isinstance(entry, dict):
                self._loadPlan(entry['name'], dict(entry['params']))
            else:
                self._loadPlan(entry)

    def startPlan(self, planName, params={}):
        self._loadPlan(planName, params, True)

    def setOptionalInputParam(self, name, value):
        for holder in self._plans.itervalues():
            holder.setOptionalInputParam(name, value)

    def setOptionalInputParams(self, **kwargs):
        for holder in self._plans.itervalues():
            holder.setOptionalInputParams(**kwargs)

    def setContext(self, context):
        for holder in self._plans.itervalues():
            holder.plan.setContext(context)

        self._context = context

    def _loadPlan(self, planName, params={}, autoStart=False):
        holder = PlanHolder(VSE.Plan(), PlanHolder.LOADING, autoStart)
        holder.params = params
        if self._context is not None:
            holder.plan.setContext(self._context)
        holder.load(planName, self._aspect, self._planTags.tags)
        self._plans[planName] = holder
        return holder


class CallableProviderType:
    ARENA = 'ARENA'
    HANGAR = 'HANGAR'
    DEATH_ZONES = 'DEATH_ZONES'
    LOOT = 'LOOT'


if IS_DEVELOPMENT:

    class CallablePlanProvider(MultiPlanProvider):
        providers = {CallableProviderType.ARENA: set(), 
           CallableProviderType.HANGAR: set(), 
           CallableProviderType.DEATH_ZONES: set(), 
           CallableProviderType.LOOT: set()}
        plansOnLoad = dict()

        def __init__(self, aspect, name, arenaBonusType=0):
            super(CallablePlanProvider, self).__init__(aspect, arenaBonusType)
            self._name = name
            self.providers.setdefault(name, set()).add(self)

        def destroy(self):
            self.providers[self._name].remove(self)

        def load(self, planNames, autoStart=False):
            super(CallablePlanProvider, self).load(planNames, autoStart)
            if self._name in self.plansOnLoad:
                for entry in self.plansOnLoad[self._name]:
                    if isinstance(entry, dict):
                        self._loadPlan(entry['name'], dict(entry['params']), autoStart)
                    else:
                        self._loadPlan(entry, {}, autoStart)


    def setPlansOnLoad(name, planNames):
        CallablePlanProvider.plansOnLoad[name] = planNames


    def startPlan(name, planName, params={}):
        if name not in CallablePlanProvider.providers:
            raise SoftException('Wrong provider name')
        for provider in CallablePlanProvider.providers[name]:
            provider.startPlan(planName, params)


def makeMultiPlanProvider(aspect, name, arenaBonusType=0):
    if IS_DEVELOPMENT:
        return CallablePlanProvider(aspect, name, arenaBonusType)
    return MultiPlanProvider(aspect, arenaBonusType)


class MultiPlanCache(object):

    def __init__(self, aspect):
        super(MultiPlanCache, self).__init__()
        self._plansBucket = {}
        self._aspect = aspect

    def destroy(self):
        for key, bucket in self._plansBucket.items():
            for vsePlans in bucket:
                vsePlans.stop()
                vsePlans.destroy()

        self._plansBucket.clear()

    def getPlan(self, componentName, planNamesAndParams):
        planNames = set(entry['name'] if isinstance(entry, dict) else entry for entry in planNamesAndParams)
        if componentName in self._plansBucket:
            for vsePlans in self._plansBucket[componentName]:
                if vsePlans.isLoaded() and all(not vsePlans.get(planName).isActive() for planName in planNames):
                    return vsePlans

        vsePlans = makeMultiPlanProvider(self._aspect, componentName)
        vsePlans.load(planNamesAndParams)
        self._plansBucket.setdefault(componentName, []).append(vsePlans)
        return vsePlans