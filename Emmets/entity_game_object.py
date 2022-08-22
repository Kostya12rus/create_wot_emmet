# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/entity_game_object.py
import BigWorld

class EntityGameObject(BigWorld.Entity):

    def __init__(self):
        self.gameObject = None
        return

    def onEnterWorld(self, *args):
        self.gameObject = self._loadGameObject()

    def onLeaveWorld(self):
        if self.gameObject is not None:
            self.gameObject.deactivate()
            self.gameObject.destroy()
            self.gameObject.stopLoading = True
            self.gameObject = None
        return

    def _loadGameObject(self):
        raise NotImplementedError

    def _registerGameObject(self, gameObject):
        self.gameObject = gameObject
        self.gameObject.setMotor(self.matrix)
        self.gameObject.activate()