# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_r.py
import typing, logging
from frameworks import wulf
_logger = logging.getLogger(__name__)

def text(resId, *args, **kwargs):
    if resId <= 0:
        _logger.warning('Invalid resId')
        return ''
    if args:
        try:
            return wulf.getTranslatedTextByResId(resId, args)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, args)
            return ''

    elif kwargs:
        try:
            return wulf.getTranslatedTextByResId(resId, kwargs)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, kwargs)
            return ''

    return wulf.getTranslatedTextByResId(resId)


def ntext(resId, n, *args, **kwargs):
    if resId <= 0:
        _logger.warning('Invalid resId')
        return ''
    if args:
        try:
            return wulf.getTranslatedPluralTextByResId(resId, n, args)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, args)
            return ''

    elif kwargs:
        try:
            return wulf.getTranslatedPluralTextByResId(resId, n, kwargs)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, kwargs)
            return ''

    return wulf.getTranslatedPluralTextByResId(resId, n)


def msgid(resId):
    return wulf.getTranslatedKey(resId)


def image(resId):
    return wulf.getImagePath(resId)


def sound(resId):
    return wulf.getSoundEffectId(resId)


def layout(resId):
    return wulf.getLayoutPath(resId)