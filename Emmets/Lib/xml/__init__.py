# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/xml/__init__.py
__all__ = [
 'dom', 'parsers', 'sax', 'etree']
_MINIMUM_XMLPLUS_VERSION = (0, 8, 4)
try:
    import _xmlplus
except ImportError:
    pass

try:
    v = _xmlplus.version_info
except AttributeError:
    pass

if v >= _MINIMUM_XMLPLUS_VERSION:
    import sys
    _xmlplus.__path__.extend(__path__)
    sys.modules[__name__] = _xmlplus
else:
    del v