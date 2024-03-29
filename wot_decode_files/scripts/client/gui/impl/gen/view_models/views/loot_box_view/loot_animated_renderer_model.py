# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_animated_renderer_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.loot_box_view.loot_def_renderer_model import LootDefRendererModel

class LootAnimatedRendererModel(LootDefRendererModel):
    __slots__ = ()
    SWF_ANIMATION = 0
    MC_ANIMATION = 1

    def __init__(self, properties=16, commands=0):
        super(LootAnimatedRendererModel, self).__init__(properties=properties, commands=commands)

    def getAnimationType(self):
        return self._getNumber(13)

    def setAnimationType(self, value):
        self._setNumber(13, value)

    def getAnimation(self):
        return self._getResource(14)

    def setAnimation(self, value):
        self._setResource(14, value)

    def getAnimationSound(self):
        return self._getResource(15)

    def setAnimationSound(self, value):
        self._setResource(15, value)

    def _initialize(self):
        super(LootAnimatedRendererModel, self)._initialize()
        self._addNumberProperty('animationType', 0)
        self._addResourceProperty('animation', R.invalid())
        self._addResourceProperty('animationSound', R.invalid())