# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/bootcamp/bootcamp_quest_widget_view.py
from bootcamp.Bootcamp import g_bootcamp
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.gen.view_models.views.bootcamp.bootcamp_quest_widget_model import BootcampQuestWidgetModel
from frameworks.wulf import WindowFlags, ViewSettings, ViewFlags
from uilogging.deprecated.bootcamp.constants import BC_LOG_KEYS, BC_LOG_ACTIONS
from uilogging.deprecated.bootcamp.loggers import BootcampLogger

class BootcampQuestWidgetView(ViewImpl):
    __slots__ = ()
    uiBootcampLogger = BootcampLogger(BC_LOG_KEYS.BC_PROGRESS_WIDGET)

    def __init__(self, flags=ViewFlags.VIEW):
        settings = ViewSettings(R.views.lobby.bootcamp.BootcampQuestWidget())
        settings.flags = flags
        settings.model = BootcampQuestWidgetModel()
        super(BootcampQuestWidgetView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BootcampQuestWidgetView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        self.__addListeners()

    def __addListeners(self):
        self.viewModel.onQuestClick += self.__onQuestClick

    def __removeListeners(self):
        self.viewModel.onQuestClick -= self.__onQuestClick

    def __onQuestClick(self):
        from gui.impl.lobby.bootcamp.bootcamp_progress_view import BootcampProgressWindow
        self.uiBootcampLogger.log(BC_LOG_ACTIONS.CLICK)
        wndFlags = WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN
        window = BootcampProgressWindow(wndFlags=wndFlags)
        window.load()

    def _onLoading(self, *args, **kwargs):
        super(BootcampQuestWidgetView, self)._onLoading()
        with self.viewModel.transaction() as (tx):
            tx.setCurrent(g_bootcamp.getLessonNum())
            tx.setTotal(g_bootcamp.getContextIntParameter('lastLessonNum'))