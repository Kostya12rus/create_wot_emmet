# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/DogTagComponent.py
import logging, BigWorld
_logger = logging.getLogger(__name__)

class DogTagComponent(BigWorld.DynamicScriptComponent):

    def set_killerDogTag(self, old):
        if self._isObserving():
            return
        else:
            _logger.info('DogTagComponent.set_killerDogTag: killerDogTag %s', str(self.killerDogTag))
            dogTagsCtrl = self.entity.guiSessionProvider.dynamic.dogTags
            if dogTagsCtrl is not None:
                dogTagsCtrl.setKillerDogTag(self.killerDogTag)
            return

    def setSlice_victimsDogTags(self, changePath, oldValue):
        if self._isObserving():
            return
        else:
            _logger.info('DogTagComponent.setSlice_victimsDogTags: victimsDogTags %s, changePath %s', str(self.victimsDogTags), str(changePath))
            dogTagsCtrl = self.entity.guiSessionProvider.dynamic.dogTags
            if dogTagsCtrl is not None:
                begin, end = changePath[0]
                newVictimsDogTags = self.victimsDogTags[begin:end]
                dogTagsCtrl.setVictimsDogTags(newVictimsDogTags)
            return

    @staticmethod
    def _isObserving():
        player_vehicle = BigWorld.player().getVehicleAttached()
        if player_vehicle is not None:
            return not player_vehicle.isPlayerVehicle
        else:
            return False