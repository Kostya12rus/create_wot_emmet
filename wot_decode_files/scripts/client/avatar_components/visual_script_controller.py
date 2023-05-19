# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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