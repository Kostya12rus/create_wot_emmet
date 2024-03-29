# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/bootcamp/bootcamp_progress_widget_view.py
from frameworks.wulf import ViewSettings, ViewFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.bootcamp.bootcamp_progress_model import BootcampProgressModel
from gui.impl.lobby.bootcamp.bootcamp_progress_base_view import BootcampProgressBaseView

class BootcampProgressWidgetView(BootcampProgressBaseView):
    __slots__ = ()

    def __init__(self, flags=ViewFlags.VIEW):
        settings = ViewSettings(R.views.lobby.bootcamp.BootcampProgressWidget())
        settings.flags = flags
        settings.model = BootcampProgressModel()
        super(BootcampProgressWidgetView, self).__init__(settings)