# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/image_view/image_view.py
from gui.Scaleform.daapi.view.meta.ImageViewMeta import ImageViewMeta
from gui.sounds.filters import switchHangarFilteredFilter
_IMAGE_ROOT_PATH = '../maps/icons/imageView'

class ImageView(ImageViewMeta):

    def __init__(self, ctx=None):
        super(ImageView, self).__init__(ctx)
        self.__image = ctx['img']

    def _populate(self):
        super(ImageView, self)._populate()
        self.setBgPath()
        switchHangarFilteredFilter(on=True)

    def onClose(self):
        self.destroy()
        switchHangarFilteredFilter(on=False)

    def setBgPath(self):
        image = ('').join((_IMAGE_ROOT_PATH, '/', self.__image))
        self.flashObject.as_setBgPath(image)