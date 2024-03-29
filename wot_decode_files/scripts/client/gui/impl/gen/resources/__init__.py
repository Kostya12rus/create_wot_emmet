# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/resources/__init__.py
from gui.impl.gen_utils import DynAccessor
from .animations import Animations
from .areas import Areas
from .atlases import Atlases
from .dynamic_ids import DynamicIds
from .entries import Entries
from .images import Images
from .sounds import Sounds
from .strings import Strings
from .styles import Styles
from .videos import Videos
from .views import Views

class Resources(object):
    __slots__ = ()
    invalid = DynAccessor(0)
    animations = Animations()
    areas = Areas()
    atlases = Atlases()
    dynamic_ids = DynamicIds()
    entries = Entries()
    images = Images()
    sounds = Sounds()
    strings = Strings()
    styles = Styles()
    videos = Videos()
    views = Views()


R = Resources()