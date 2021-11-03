# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/fo_precache.py
import BigWorld
from debug_utils import LOG_ERROR, LOG_DEBUG
_IS_ENABLED = True
if _IS_ENABLED:

    def add(path, forced=False):
        result = True
        try:
            result = BigWorld.wg_precacheScaleformResource(path, forced)
            if result:
                LOG_DEBUG('Resource is added to precache', path)
        except AttributeError:
            LOG_ERROR('BigWorld package does not include function wg_precacheScaleformResource')

        return result


    def clear(path=''):
        try:
            BigWorld.wg_eraseScaleformResFromCache(path)
            LOG_DEBUG('Resource(s) is(are) cleared from precache', path)
        except AttributeError:
            LOG_ERROR('BigWorld package does not include function wg_eraseScaleformResFromCache')


else:

    def add(path, forced=False):
        return True


    def clear(path=''):
        pass