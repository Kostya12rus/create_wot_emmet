# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/mapbox_entry_point.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.MapBoxEntryPointMeta import MapBoxEntryPointMeta
from gui.impl.lobby.mapbox.mapbox_entry_point_view import MapBoxEntryPointView

class MapBoxEntryPoint(MapBoxEntryPointMeta):

    def _makeInjectView(self):
        self.__view = MapBoxEntryPointView(ViewFlags.COMPONENT)
        return self.__view