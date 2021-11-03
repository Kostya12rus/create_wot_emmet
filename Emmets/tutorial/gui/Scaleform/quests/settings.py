# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/quests/settings.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates
from tutorial.gui.Scaleform.quests import pop_ups

class TUTORIAL_VIEW_ALIAS(object):
    TUTORIAL_QUEST_AWARD_WINDOW = 'tQuestAwardWindow'


QUESTS_VIEW_SETTINGS = (
 GroupedViewSettings(TUTORIAL_VIEW_ALIAS.TUTORIAL_QUEST_AWARD_WINDOW, pop_ups.TutorialQuestAwardWindow, 'awardWindow.swf', WindowLayer.WINDOW, 'tQuestAwardGroup', None, ScopeTemplates.DEFAULT_SCOPE),)
WINDOW_ALIAS_MAP = {'awardWindow': TUTORIAL_VIEW_ALIAS.TUTORIAL_QUEST_AWARD_WINDOW}