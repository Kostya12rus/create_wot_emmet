# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/uniprof/__init__.py
import BigWorld
__all__ = ('regionDecorator', 'enterToRegion', 'exitFromRegion')

def _isRegionSupported():
    if not hasattr(BigWorld, 'uniprofRegionEnter'):
        return False
    if not hasattr(BigWorld, 'uniprofRegionExit'):
        return False
    return True


_IS_REGION_SUPPORTED = _isRegionSupported()
if _IS_REGION_SUPPORTED:
    from .regions import regionDecorator
    from .regions import enterToRegion, exitFromRegion
else:

    class _DummyDecorator(object):
        __slots__ = ()

        def __call__(self, func):
            return func


    def enterToRegion(*_):
        pass


    def exitFromRegion(*_):
        pass


    def regionDecorator(*_, **__):
        return _DummyDecorator()