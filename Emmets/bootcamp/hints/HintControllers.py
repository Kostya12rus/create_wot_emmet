# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/hints/HintControllers.py
import base64, cPickle
from functools import partial
import BattleReplay, BigWorld, SoundGroups
from bootcamp.BootcampConstants import HINT_TYPE
from BattleReplay import CallbackDataNames
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from helpers import dependency
from helpers.i18n import makeString
from skeletons.gui.game_control import IBootcampController

class PrimaryHintController(object):
    HINT_HIGHLIGHTS = {HINT_TYPE.HINT_REPAIR_TRACK: 'InBattleRepairKit', 
       HINT_TYPE.HINT_HEAL_CREW: 'InBattleHealKit', 
       HINT_TYPE.HINT_USE_EXTINGUISHER: 'InBattleExtinguisher'}
    SHOW_SOUND_ID = 'bc_main_tips_activity_start'
    COMPLETE_SOUND_ID = 'bc_main_tips_activity'
    HIDE_SOUND_ID = 'bc_main_tips_activity_done'
    TASK_START_SOUND_ID = 'bc_main_tips_activity_start'
    TASK_DONE_SOUND_ID = 'bc_main_tips_activity_done'
    HINT_IDS_TO_MUTE = tuple()
    HINT_IDS_TO_COMPLETE = (
     HINT_TYPE.HINT_MOVE, HINT_TYPE.HINT_MOVE_TURRET, HINT_TYPE.HINT_SHOOT, HINT_TYPE.HINT_ROTATE_LOBBY)

    def __init__(self, system, hintId, typeId, completed, timeCompleted, timeCooldown, message, voiceover):
        super(PrimaryHintController, self).__init__()
        self.id = hintId
        self.typeId = typeId
        self.voiceover = voiceover
        self.timeCooldown = timeCooldown
        self._isOnScreen = False
        self._completed = completed
        self._hideCallbackId = None
        self._timeout = timeCompleted
        self.message = message
        self.muted = False
        self._hintSystem = system
        if self.typeId in HINT_TYPE.BATTLE_HINTS:
            self._scope = EVENT_BUS_SCOPE.BATTLE
            self._viewAlias = VIEW_ALIAS.BOOTCAMP_BATTLE_TOP_HINT
        else:
            self._viewAlias = VIEW_ALIAS.BOOTCAMP_TOOLTIPS_WINDOW
            self._scope = EVENT_BUS_SCOPE.LOBBY
        return

    def show(self):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(self._viewAlias), ctx={'id': self.typeId, 
           'completed': self._completed, 'message': self.message, 
           'hideCallback': self.onHided}), self._scope)
        if self._completed:
            self.hideWithTimeout()
        if self.typeId == HINT_TYPE.HINT_SNIPER_LEVEL0:
            self.playSound(self.TASK_DONE_SOUND_ID)
        if self.typeId in self.HINT_IDS_TO_COMPLETE:
            if not self._completed:
                self.playSound(self.TASK_START_SOUND_ID)
            else:
                self.playSound(self.TASK_DONE_SOUND_ID)
        else:
            self.playSound(self.SHOW_SOUND_ID)
        if self.typeId in PrimaryHintController.HINT_HIGHLIGHTS:
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_ADD_HIGHLIGHT), ctx=PrimaryHintController.HINT_HIGHLIGHTS[self.typeId]), EVENT_BUS_SCOPE.BATTLE)
        self._isOnScreen = True
        if self.voiceover and not self.muted:
            self._hintSystem.playVoiceover(self.voiceover)

    def hideWithTimeout(self):
        if self._hideCallbackId:
            BigWorld.cancelCallback(self._hideCallbackId)
            self._hideCallbackId = None
        if self._timeout:
            self._hideCallbackId = BigWorld.callback(self._timeout, self.hide)
        return

    def hide(self):
        self._hideCallbackId = None
        if self.typeId not in self.HINT_IDS_TO_COMPLETE:
            self.playSound(self.HIDE_SOUND_ID)
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_HINT_HIDE, self.typeId)), self._scope)
        if self.typeId in PrimaryHintController.HINT_HIGHLIGHTS:
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_REMOVE_HIGHLIGHT), ctx=PrimaryHintController.HINT_HIGHLIGHTS[self.typeId]), EVENT_BUS_SCOPE.BATTLE)
        return

    def complete(self):
        if not self._completed:
            self._completed = True
            if self._isOnScreen:
                g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_HINT_COMPLETE, self.typeId)), self._scope)
                self.hideWithTimeout()
                if self.typeId in self.HINT_IDS_TO_COMPLETE:
                    self.playSound(self.TASK_DONE_SOUND_ID)
                else:
                    self.playSound(self.COMPLETE_SOUND_ID)

    def isComplete(self):
        return self._completed

    def isShown(self):
        return self._isOnScreen

    def isReadyToClose(self):
        if not self._completed:
            return False
        return not self._isOnScreen

    def onHided(self):
        self._isOnScreen = False

    def close(self):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_HINT_CLOSE)), self._scope)
        if self.typeId in PrimaryHintController.HINT_HIGHLIGHTS:
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_REMOVE_HIGHLIGHT), ctx=PrimaryHintController.HINT_HIGHLIGHTS[self.typeId]), EVENT_BUS_SCOPE.BATTLE)
        if self.voiceover and not self.muted:
            self._hintSystem.unscheduleVoiceover(self.voiceover)
        if self._hideCallbackId:
            BigWorld.cancelCallback(self._hideCallbackId)
            self._hideCallbackId = None
        return

    def playSound(self, sound_id):
        if self.typeId not in self.HINT_IDS_TO_MUTE and not self.muted:
            SoundGroups.g_instance.playSound2D(sound_id)


class SecondaryHintController(object):
    HINT_HIGHLIGHTS = {HINT_TYPE.HINT_LOW_HP: 'DamagePanelHealthbar'}

    def __init__(self, system, hintId, typeId, message):
        super(SecondaryHintController, self).__init__()
        self.id = hintId
        self._typeId = typeId
        self._message = makeString(message)
        self._onScreen = False

    def isShown(self):
        return self._onScreen

    def show(self):
        if not self._onScreen:
            g_eventBus.handleEvent(events.BootcampEvent(events.BootcampEvent.SHOW_SECONDARY_HINT, self._typeId, self._message), EVENT_BUS_SCOPE.BATTLE)
            self._onScreen = True
            if self._typeId in SecondaryHintController.HINT_HIGHLIGHTS:
                g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_ADD_HIGHLIGHT), ctx=SecondaryHintController.HINT_HIGHLIGHTS[self._typeId]), EVENT_BUS_SCOPE.BATTLE)

    def hide(self):
        if self._onScreen:
            if self._typeId in SecondaryHintController.HINT_HIGHLIGHTS:
                g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_REMOVE_HIGHLIGHT), ctx=SecondaryHintController.HINT_HIGHLIGHTS[self._typeId]), EVENT_BUS_SCOPE.BATTLE)
            g_eventBus.handleEvent(events.BootcampEvent(events.BootcampEvent.HIDE_SECONDARY_HINT, None, None), EVENT_BUS_SCOPE.BATTLE)
            self._onScreen = False
        return


class PrimaryHintControllerReplayRecorder(PrimaryHintController):

    def show(self):
        super(PrimaryHintControllerReplayRecorder, self).show()
        self.serializeMethod(CallbackDataNames.BC_HINT_SHOW, (
         self.id, self.typeId, self._completed, self.message, self.voiceover))

    def hide(self):
        super(PrimaryHintControllerReplayRecorder, self).hide()
        self.serializeMethod(CallbackDataNames.BC_HINT_HIDE, (
         self.id, self.typeId, self._completed, self.message, self.voiceover))

    def complete(self):
        super(PrimaryHintControllerReplayRecorder, self).complete()
        self.serializeMethod(CallbackDataNames.BC_HINT_COMPLETE, (
         self.id, self.typeId, self._completed, self.message, self.voiceover))

    def close(self):
        super(PrimaryHintControllerReplayRecorder, self).close()
        self.serializeMethod(CallbackDataNames.BC_HINT_CLOSE, (
         self.id, self.typeId, self._completed, self.message, self.voiceover))

    def onHided(self):
        super(PrimaryHintControllerReplayRecorder, self).onHided()
        self.serializeMethod(CallbackDataNames.BC_HINT_ONHIDED, (
         self.id, self.typeId, self._completed, self.message, self.voiceover))

    def serializeMethod(self, eventName, params):
        BattleReplay.g_replayCtrl.serializeCallbackData(eventName, (base64.b64encode(cPickle.dumps(params, -1)),))


class ReplayHintPlaySystem:
    bootcamp = dependency.descriptor(IBootcampController)
    COMMAND_SHOW = 1
    COMMAND_HIDE = 2
    COMMAND_COMPLETE = 3
    COMMAND_CLOSE = 4
    COMMAND_HIDED = 5

    def __init__(self, hintSystem):
        self.replayCallbacks = []
        self.__commandBuffer = []
        self.__hints = {}
        self.__hintSystem = hintSystem
        self.replaySubscribe()

    def destroy(self):
        for hint in self.__hints.itervalues():
            hint.close()

        self.__hints.clear()
        if self.bootcamp.replayCtrl:
            for eventName, callback in self.replayCallbacks:
                self.bootcamp.replayCtrl.delDataCallback(eventName, callback)

        self.replayCallbacks = []
        self.__hintSystem = None
        return

    def update(self):
        while self.__commandBuffer:
            command, id, typeId, completed, message, voiceover, muted = self.__commandBuffer[0]
            if command == ReplayHintPlaySystem.COMMAND_SHOW:
                self.__hints[id] = PrimaryHintController(self.__hintSystem, id, typeId, completed, 0, 0, message, voiceover)
                self.__hints[id].muted = muted
                self.__hints[id].show()
            elif command == ReplayHintPlaySystem.COMMAND_HIDE:
                self.__hints[id].hide()
            elif command == ReplayHintPlaySystem.COMMAND_COMPLETE:
                self.__hints[id].typeId = typeId
                self.__hints[id].message = message
                self.__hints[id].voiceover = voiceover
                self.__hints[id].muted = muted
                self.__hints[id].complete()
            elif command == ReplayHintPlaySystem.COMMAND_CLOSE:
                if id in self.__hints:
                    self.__hints[id].close()
                    del self.__hints[id]
            elif command == ReplayHintPlaySystem.COMMAND_HIDED:
                if id in self.__hints:
                    self.__hints[id].onHided()
            del self.__commandBuffer[0]

    def replaySubscribe(self):
        self.replayMethodSubscribe(CallbackDataNames.BC_HINT_SHOW, ReplayHintPlaySystem.COMMAND_SHOW)
        self.replayMethodSubscribe(CallbackDataNames.BC_HINT_HIDE, ReplayHintPlaySystem.COMMAND_HIDE)
        self.replayMethodSubscribe(CallbackDataNames.BC_HINT_COMPLETE, ReplayHintPlaySystem.COMMAND_COMPLETE)
        self.replayMethodSubscribe(CallbackDataNames.BC_HINT_CLOSE, ReplayHintPlaySystem.COMMAND_CLOSE)
        self.replayMethodSubscribe(CallbackDataNames.BC_HINT_ONHIDED, ReplayHintPlaySystem.COMMAND_HIDED)

    def appendCommandBuffer(self, command, id, typeId, completed, message, voiceover):
        mute = BattleReplay.g_replayCtrl.isTimeWarpInProgress
        self.__commandBuffer.append((command, id, typeId, completed, message, voiceover, mute))

    def replayMethodSubscribe(self, eventName, command):
        callback = partial(self.replayMethodCall, command, eventName)
        if self.bootcamp.replayCtrl:
            self.bootcamp.replayCtrl.setDataCallback(eventName, callback)
        self.replayCallbacks.append((eventName, callback))

    def replayMethodCall(self, command, eventName, binData):
        self.appendCommandBuffer(command, *cPickle.loads(base64.b64decode(binData)))


def createPrimaryHintController(system, hintId, typeId, completed, timeCompleted, timeCooldown, message, voiceover):
    if BattleReplay.g_replayCtrl.isRecording:
        return PrimaryHintControllerReplayRecorder(system, hintId, typeId, completed, timeCompleted, timeCooldown, message, voiceover)
    return PrimaryHintController(system, hintId, typeId, completed, timeCompleted, timeCooldown, message, voiceover)


def createSecondaryHintController(system, hintId, typeId, message):
    return SecondaryHintController(system, hintId, typeId, message)


def createReplayPlayHintSystem(hintSystem):
    if BattleReplay.g_replayCtrl.isPlaying:
        return ReplayHintPlaySystem(hintSystem)
    else:
        return