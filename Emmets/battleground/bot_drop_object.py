# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/battleground/bot_drop_object.py
import logging
from functools import partial
import AnimationSequence, BigWorld, Math, CGF
from constants import AirdropType
from helpers import dependency
import BattleReplay
from ReplayEvents import g_replayEvents
from battleground.components import SequenceComponent
from battleground.iself_assembler import ISelfAssembler
from helpers.CallbackDelayer import CallbackDelayer
from items import vehicles
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider
from cgf_obsolete_script.script_game_object import ScriptGameObject
from vehicle_systems.stricted_loading import makeCallbackWeak
_logger = logging.getLogger(__name__)

class BotAirdrop(ScriptGameObject, CallbackDelayer, ISelfAssembler):
    __dynamicObjectsCache = dependency.descriptor(IBattleDynamicObjectsCache)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    ALTITUDE_CORRECTING = 0.5
    END_ANIMATION_TIME_CORRECTING = 0.18
    __slots__ = ('owner', '__deliveryPosition', '__markerArea', '__deliveryEffect',
                 '__teamID', '__yawAxis', '__plannedAnimDuration', '__deliveryTime')
    TYPE_TO_EQUIPMENT = {AirdropType.BOT: 'spawn_kamikaze', AirdropType.BOT_CLING: 'clingBrander'}

    def __init__(self, dropID, deliveryPosition, teamID, yawAxis, deliveryTime, airdropType):
        self.__spaceID = BigWorld.player().spaceID
        ScriptGameObject.__init__(self, self.__spaceID)
        CallbackDelayer.__init__(self)
        self.__deliveryTime = deliveryTime
        self.__deliveryPosition = deliveryPosition
        self.__markerArea = None
        self.__deliveryEffect = None
        self.__teamID = teamID
        self.__yawAxis = yawAxis
        self.__plannedAnimDuration = 0.0
        self.__airdropType = airdropType
        return

    def start(self, *args, **kwargs):
        config = self.__dynamicObjectsCache.getConfig(BigWorld.player().arenaGuiType)
        equipmentDescr = self.__getEquipmentDescr()
        self.__markerArea = self.__createMarkerArea(config, equipmentDescr)
        deliveryAnimationStartDelay = equipmentDescr.clientVisuals.deliveringAnimationStartDelay
        self.__plannedAnimDuration = equipmentDescr.delay - deliveryAnimationStartDelay
        timeToSpawn = self.__deliveryTime - BigWorld.serverTime()
        plannedAnimDuration = equipmentDescr.delay - equipmentDescr.clientVisuals.deliveringAnimationStartDelay
        timeToStartDeliveryAnim = timeToSpawn - plannedAnimDuration
        if BattleReplay.g_replayCtrl.isPlaying:
            g_replayEvents.onTimeWarpStart += self.__onReplayTimeWarpStart
        if self.__markerArea:
            self.delayCallback(equipmentDescr.delay, self.__removeMarkerArea)
        if timeToStartDeliveryAnim > 0:
            self.delayCallback(timeToStartDeliveryAnim, partial(self.__createDeliveryEffect, config))
        else:
            _logger.error('Delivery animation of Kamikaze will not be playing, no time for it!')
        self.activate()
        self.transferOwnershipToWorld()

    def destroy(self):
        super(BotAirdrop, self).destroy()
        CallbackDelayer.destroy(self)
        if BattleReplay.g_replayCtrl.isPlaying:
            g_replayEvents.onTimeWarpStart -= self.__onReplayTimeWarpStart
        self.__removeMarkerArea()
        self.__removeDeliveryEffect()
        ScriptGameObject.destroy(self)
        CallbackDelayer.destroy(self)

    def __onReplayTimeWarpStart(self):
        self.__removeMarkerArea()
        self.__removeDeliveryEffect()

    def __getEffect(self, effects):
        if self.__sessionProvider.getArenaDP().isAllyTeam(self.__teamID):
            return effects.ally
        return effects.enemy

    def __createMarkerArea(self, config, equipmentDescr):
        markerArea = CGF.GameObject(self.__spaceID)
        effect3D = self.__getEffect(config.getBotDeliveryMarker())
        if effect3D is not None:
            effectPath = effect3D.path
            markerTerrainPosition = self.__deliveryPosition - equipmentDescr.botSpawnPointOffset
            BigWorld.loadResourceListBG((AnimationSequence.Loader(effectPath, self.__spaceID),), makeCallbackWeak(self.__on3dEffectLoaded, equipmentDescr, effectPath, markerTerrainPosition))
            return markerArea
        else:
            _logger.error('Marker Effect is not defined!')
            return

    def __on3dEffectLoaded(self, equipmentDescr, effectP, position, resourceRefs):
        markerArea = self.__markerArea
        if effectP in resourceRefs.failedIDs or markerArea is None:
            return
        clientVisuals = equipmentDescr.clientVisuals
        sequenceComponent = markerArea.createComponent(SequenceComponent, resourceRefs[effectP])
        sequenceComponent.createTerrainEffect(position + clientVisuals.markerPositionOffset, scale=clientVisuals.markerScale, loopCount=-1)
        markerArea.activate()
        return

    def __createDeliveryEffect(self, config):
        if self.__airdropType == AirdropType.BOT_CLING:
            effect = self.__getEffect(config.getBotClingDeliveryEffect())
        else:
            effect = self.__getEffect(config.getBotDeliveryEffect())
        if effect is not None:
            effectPath = effect.path
            BigWorld.loadResourceListBG((
             AnimationSequence.Loader(effectPath, self.__spaceID),), makeCallbackWeak(self.__onDeliverEffectLoaded, effectPath, self.__deliveryPosition))
            return
        else:
            return

    def __onDeliverEffectLoaded(self, effectP, position, resourceRefs):
        if effectP in resourceRefs.failedIDs:
            _logger.error('Effect %s has not been loaded!', effectP)
            return
        effectAnimation = CGF.GameObject(self.__spaceID)
        sequenceComponent = effectAnimation.createComponent(SequenceComponent, resourceRefs[effectP])
        correctedPosition = position + Math.Vector3(0, self.ALTITUDE_CORRECTING, 0)
        sequenceComponent.createTerrainEffect(correctedPosition, loopCount=1, rotation=(self.__yawAxis, 0, 0))
        effectAnimation.activate()
        self.__deliveryEffect = effectAnimation
        timeToSpawn = self.__deliveryTime - BigWorld.serverTime()
        self.delayCallback(timeToSpawn + self.END_ANIMATION_TIME_CORRECTING, self.__removeDeliveryEffect)

    def __removeMarkerArea(self):
        if self.__markerArea is not None:
            self.__markerArea.destroy()
        self.__markerArea = None
        return

    def __removeDeliveryEffect(self):
        if self.__deliveryEffect is not None:
            self.__deliveryEffect.destroy()
        self.__deliveryEffect = None
        return

    def __getEquipmentDescr(self):
        name = BotAirdrop.TYPE_TO_EQUIPMENT[self.__airdropType]
        return vehicles.g_cache.equipments()[vehicles.g_cache.equipmentIDs()[name]]