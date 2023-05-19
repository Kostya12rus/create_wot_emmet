# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/bootcamp_progress_component.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.prb_control.entities.listener import IGlobalListener
from gui.impl.lobby.bootcamp.bootcamp_progress_widget_view import BootcampProgressWidgetView
from gui.Scaleform.daapi.view.meta.BootcampProgressMeta import BootcampProgressMeta

class BootcampProgressComponent(InjectComponentAdaptor, BootcampProgressMeta, IGlobalListener):

    def _makeInjectView(self):
        return BootcampProgressWidgetView(flags=ViewFlags.COMPONENT)