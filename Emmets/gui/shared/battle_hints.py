# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/battle_hints.py
import logging
from collections import namedtuple
import ResMgr
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
_logger = logging.getLogger(__name__)
_CONFIG_FILE = 'gui/battle_hints.xml'

class BattleHintData(namedtuple('_HintData', ('name', 'componentAlias', 'iconPath', 'duration', 'maxWaitTime',
                         'dynamicFields', 'priority', 'soundFx', 'soundNotification',
                         'htmlTemplate'))):

    def makeVO(self, data=None):
        if not data:
            data = {}
        message = makeHtmlString('html_templates:battleHints', self.htmlTemplate)
        message = self._applyDataParams(message, data)
        hasIcon = self.iconPath and 'battleHints' in R.images.gui.maps.icons.keys()
        return {'message': message, 
           'iconSource': backport.image(R.images.gui.maps.icons.battleHints.event.dyn(self.iconPath)()) if hasIcon else None}

    def _applyDataParams(self, message, data):
        try:
            return message.format(**data)
        except KeyError:
            _logger.error('BattleHintData::_applyDataParams: Incorrect format for: %s', str(data))
            return message


def makeHintsData():
    battleHintsConfig = ResMgr.openSection(_CONFIG_FILE)
    hints = []
    if battleHintsConfig:
        for hint in battleHintsConfig.values():
            hints.append(BattleHintData(name=hint['name'].asString, componentAlias=hint['component'].asString, htmlTemplate=hint['htmlTemplate'].asString, iconPath=hint['iconPath'].asString if hint.has_key('iconPath') else None, duration=hint['duration'].asFloat if hint.has_key('duration') else None, maxWaitTime=hint['maxWaitTime'].asFloat if hint.has_key('maxWaitTime') else 10, dynamicFields=hint['dynamicData'].asString.split() if hint.has_key('dynamicData') else [], priority=hint['priority'].asInt if hint.has_key('priority') else 0, soundFx=hint['soundFx'].asString if hint.has_key('soundFx') else None, soundNotification=hint['soundNotification'].asString if hint.has_key('soundNotification') else None))

    else:
        _logger.error('Failed to open: %s', _CONFIG_FILE)
    return hints