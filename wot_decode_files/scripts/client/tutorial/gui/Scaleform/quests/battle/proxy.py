# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/quests/battle/proxy.py
from tutorial.gui import GUIProxy

class BattleQuestsProxy(GUIProxy):

    def init(self):
        self.onGUILoaded()
        return True

    def fini(self):
        self.eManager.clear()

    def clear(self):
        self.clearChapterInfo()

    def getSceneID(self):
        return 'Battle'

    def playEffect(self, effectName, args):
        return False

    def isEffectRunning(self, effectName, effectID=None, effectSubType=None):
        return False