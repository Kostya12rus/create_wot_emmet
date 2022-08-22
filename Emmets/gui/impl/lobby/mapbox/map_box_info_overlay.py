# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mapbox/map_box_info_overlay.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.impl.lobby.mapbox.sound import getMapboxViewSoundSpace

class MapBoxInfoOverlay(WebView):
    _COMMON_SOUND_SPACE = getMapboxViewSoundSpace()