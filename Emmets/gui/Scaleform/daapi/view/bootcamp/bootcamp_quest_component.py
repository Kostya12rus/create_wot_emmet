# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/bootcamp_quest_component.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.bootcamp.bootcamp_quest_widget_view import BootcampQuestWidgetView
from gui.Scaleform.daapi.view.meta.DailyQuestMeta import DailyQuestMeta

class BootcampQuestComponent(InjectComponentAdaptor, DailyQuestMeta):

    def _makeInjectView(self):
        return BootcampQuestWidgetView(flags=ViewFlags.COMPONENT)

    def updateWidgetLayout(self, value):
        pass