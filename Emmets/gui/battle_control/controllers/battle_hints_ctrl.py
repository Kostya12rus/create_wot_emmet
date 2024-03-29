# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/battle_hints_ctrl.py
import time, logging
from collections import namedtuple
import BigWorld, SoundGroups, constants
from gui.battle_control.view_components import ViewComponentsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.shared import battle_hints
from shared_utils import findFirst
_logger = logging.getLogger(__name__)
HintRequest = namedtuple('HintRequest', ('hint', 'data', 'requestTime'))

class BattleHintComponent(object):
    _HINT_MIN_SHOW_TIME = 2.0

    def __init__(self):
        super(BattleHintComponent, self).__init__()
        self.__currentHint = None
        self.__hintStartTime = 0
        self.__hintRequests = []
        self.__hideCallback = None
        return

    def showHint(self, hint, data):
        currentHint = self.__currentHint
        if currentHint:
            requestTime = time.time()
            self.__hintRequests.append(HintRequest(hint, data, requestTime))
            if hint.priority > currentHint.priority:
                showTimeLeft = self._HINT_MIN_SHOW_TIME - (time.time() - self.__hintStartTime)
                if showTimeLeft <= 0:
                    self.__hideCurrentHint()
                else:
                    self.__hideHintCallback()
                    self.__hideCallback = BigWorld.callback(showTimeLeft, self.__hideCurrentHint)
        else:
            self.__showHint(hint, data)

    def hideHint(self, hint=None):
        if hint is None or self.__currentHint == hint:
            self.__hideCurrentHint()
        else:
            _logger.warning('Failed to hide hint name=%s', hint.name)
        return

    def _showHint(self, hintData):
        raise NotImplementedError

    def _hideHint(self):
        raise NotImplementedError

    def _getSoundNotification(self, hint, data):
        return hint.soundNotification

    def __showHint(self, hint, data):
        if hint.soundFx is not None:
            SoundGroups.g_instance.playSound2D(hint.soundFx)
        sound = self._getSoundNotification(hint, data)
        if sound is not None:
            player = BigWorld.player()
            if hasattr(player, 'soundNotifications'):
                soundNotifications = player.soundNotifications
                if soundNotifications is not None:
                    soundNotifications.play(sound)
        _logger.debug('Show battle hint hintName=%s, priority=%d', hint.name, hint.priority)
        self._showHint(hint.makeVO(data))
        self.__currentHint = hint
        self.__hintStartTime = time.time()
        duration = hint.duration
        if duration is not None:
            self.__hideHintCallback()
            self.__hideCallback = BigWorld.callback(duration, self.__hideCurrentHint)
        return

    def __hideCurrentHint(self):
        self.__hideHintCallback()
        self._hideHint()
        self.__currentHint = None
        self.__showDelayedHint()
        return

    def __hideHintCallback(self):
        if self.__hideCallback is not None:
            BigWorld.cancelCallback(self.__hideCallback)
            self.__hideCallback = None
        return

    def __showDelayedHint(self):
        currentTime = time.time()
        self.__hintRequests = [ r for r in self.__hintRequests if currentTime - r.requestTime < r.hint.maxWaitTime ]
        delayedHints = self.__hintRequests
        if not delayedHints:
            return
        maxPriorityHint = max(delayedHints, key=(lambda r: r.hint.priority))
        delayedHints.remove(maxPriorityHint)
        hint, data, _ = maxPriorityHint
        self.__showHint(hint, data)


class BattleHintsController(ViewComponentsController):
    _DEFAULT_HINT_NAME = 'default'

    def __init__(self, hintsData):
        super(BattleHintsController, self).__init__()
        self.__hintsData = {hint.name: hint for hint in hintsData}

    def getControllerID(self):
        return BATTLE_CTRL_ID.BATTLE_HINTS

    def startControl(self, *args):
        pass

    def stopControl(self):
        pass

    def showHint(self, hintName, data=None):
        component, hint = self.__getComponentAndHint(hintName)
        if hint and component:
            _logger.debug('Request battle hint hintName=%s, priority=%d', hint.name, hint.priority)
            component.showHint(hint, data)
        else:
            _logger.error('Failed to show hint name=%s', hintName)

    def hideHint(self, hintName):
        component, hint = self.__getComponentAndHint(hintName)
        if hint and component:
            component.hideHint(hint)
        else:
            _logger.error('Failed to hide hint name=%s', hintName)

    def __getComponentAndHint(self, hintName):
        component = None
        hint = self.__hintsData.get(hintName)
        if hint is None and constants.IS_DEVELOPMENT:
            hint = self.__hintsData.get(self._DEFAULT_HINT_NAME)
            hint = hint._replace(rawMessage=hintName)
        if hint:
            alias = hint.componentAlias
            component = findFirst((lambda comp: comp.getAlias() == alias), self._viewComponents)
            if not component:
                _logger.error('Unknown component alias=%s', alias)
        else:
            _logger.error('Unknown hint name=%s', hintName)
        return (component, hint)


def createBattleHintsController():
    return BattleHintsController(battle_hints.makeHintsData())