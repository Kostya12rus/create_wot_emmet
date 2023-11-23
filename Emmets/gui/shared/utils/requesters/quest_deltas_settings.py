# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/quest_deltas_settings.py
from UserDict import IterableUserDict
import typing
from account_helpers import AccountSettings
from account_helpers.AccountSettings import QUEST_DELTAS, QUESTS
if typing.TYPE_CHECKING:
    from typing import Hashable, Any

class QuestDeltasSettings(IterableUserDict):

    def __init__(self, subKey=''):
        IterableUserDict.__init__(self)
        self._subKey = subKey
        savedSettings = AccountSettings.getSettings(QUESTS).get(QUEST_DELTAS, dict()).get(self._subKey)
        if savedSettings is None:
            return
        else:
            for k, v in savedSettings.iteritems():
                self.data[k] = v

            return

    def __setitem__(self, key, item):
        IterableUserDict.__setitem__(self, key, item)
        self._saveToSettings()

    def __delitem__(self, key):
        IterableUserDict.__delitem__(self, key)
        self._saveToSettings()

    def _saveToSettings(self):
        savedDict = {k: v for k, v in self.data.iteritems()}
        questSettings = AccountSettings.getSettings(QUESTS)
        questSettings.get(QUEST_DELTAS, dict())[self._subKey] = savedDict
        AccountSettings.setSettings(QUESTS, questSettings)