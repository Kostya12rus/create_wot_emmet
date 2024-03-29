# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/effect_types.py
from frameworks.wulf import ViewModel

class EffectTypes(ViewModel):
    __slots__ = ()
    HINT = 'hint'
    BOOTCAMP_HINT = 'bootcampHint'
    DISPLAY = 'display'
    TWEEN = 'tween'
    CLIP = 'clip'
    ENABLED = 'enabled'
    OVERLAY = 'overlay'
    DEFAULT_OVERLAY = 'defaultOverlay'
    LAYOUT = 'layout'

    def __init__(self, properties=0, commands=0):
        super(EffectTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(EffectTypes, self)._initialize()