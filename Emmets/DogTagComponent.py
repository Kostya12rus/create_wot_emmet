# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/DogTagComponent.py
import logging, BigWorld, BattleReplay
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
        if BattleReplay.isServerSideReplay():
            return True
        return not BigWorld.player().vehicle.isPlayerVehicle