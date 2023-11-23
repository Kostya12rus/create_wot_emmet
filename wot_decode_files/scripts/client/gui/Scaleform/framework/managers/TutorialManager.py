# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/managers/TutorialManager.py
from Event import Event, EventManager
from gui.Scaleform.framework.entities.abstract.TutorialManagerMeta import TutorialManagerMeta

class ScaleformTutorialManager(TutorialManagerMeta):

    def __init__(self):
        super(ScaleformTutorialManager, self).__init__()
        self.__eventMgr = EventManager()
        self.onComponentFoundEvent = Event(self.__eventMgr)
        self.onComponentDisposedEvent = Event(self.__eventMgr)
        self.onTriggerActivatedEvent = Event(self.__eventMgr)
        self.onEffectCompletedEvent = Event(self.__eventMgr)

    def _dispose(self):
        self.__eventMgr.clear()
        super(ScaleformTutorialManager, self)._dispose()

    def onComponentFound(self, componentId, viewTutorialId):
        self.onComponentFoundEvent(componentId, viewTutorialId)

    def onTriggerActivated(self, componentId, triggerId, state):
        self.onTriggerActivatedEvent(componentId, triggerId, state)

    def onComponentDisposed(self, componentId):
        self.onComponentDisposedEvent(componentId)

    def onEffectCompleted(self, componentId, effectType):
        self.onEffectCompletedEvent(componentId, effectType)