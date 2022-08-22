# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/bootcamp_progress_component.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.prb_control.entities.listener import IGlobalListener
from gui.impl.lobby.bootcamp.bootcamp_progress_widget_view import BootcampProgressWidgetView
from gui.Scaleform.daapi.view.meta.BootcampProgressMeta import BootcampProgressMeta

class BootcampProgressComponent(InjectComponentAdaptor, BootcampProgressMeta, IGlobalListener):

    def _makeInjectView(self):
        return BootcampProgressWidgetView(flags=ViewFlags.COMPONENT)