# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/common/settings/mixins.py
import typing
from frameworks.wulf import WindowLayer
if typing.TYPE_CHECKING:
    from gui.Scaleform.framework.managers import ContainerManager
_LAYERS = [
 WindowLayer.FULLSCREEN_WINDOW, WindowLayer.CURSOR, WindowLayer.WAITING, WindowLayer.SERVICE_LAYOUT]

class LayerVisibilityMixin(object):

    def __init__(self, *args, **kwargs):
        super(LayerVisibilityMixin, self).__init__(*args, **kwargs)
        self.__previouslyVisibleLayers = None
        return

    def _populate(self):
        super(LayerVisibilityMixin, self)._populate()
        containerManager = self.app.containerManager
        self.__previouslyVisibleLayers = containerManager.getVisibleLayers()
        containerManager.setVisibleLayers(_LAYERS)

    def _dispose(self):
        super(LayerVisibilityMixin, self)._dispose()
        containerManager = self.app.containerManager
        containerManager.setVisibleLayers(self.__previouslyVisibleLayers)
        self.__previouslyVisibleLayers = None
        return