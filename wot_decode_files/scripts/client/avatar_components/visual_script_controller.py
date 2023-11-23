# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/visual_script_controller.py
import cPickle, VSE

class VisualScriptController(object):

    def __init__(self):
        self.__enabled = False

    def onBecomePlayer(self):
        self.__enabled = True

    def onBecomeNonPlayer(self):
        self.__enabled = False

    def handleKey(self, isDown, key, mods):
        pass

    def handleScriptEventFromServer(self, eventName, planName, params, targetAspects, eventScope):
        if self.__enabled:
            if eventScope.startswith('ArenaT:') and self.arena is not None:
                eventScope = 'ArenaT:' + str(self.arena.arenaUniqueID)
            VSE.passEventToVisualScript(eventName, planName, cPickle.loads(params), targetAspects, eventScope)
        return