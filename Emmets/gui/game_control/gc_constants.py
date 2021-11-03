# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/gc_constants.py
from shared_utils import CONST_CONTAINER

class BROWSER(CONST_CONTAINER):
    SIZE = (990, 550)
    VIDEO_SIZE = (864, 486)


class PROMO(CONST_CONTAINER):

    class TEMPLATE(CONST_CONTAINER):
        PATCH = 'promo_patchnote'
        ACTION = 'promo_action'