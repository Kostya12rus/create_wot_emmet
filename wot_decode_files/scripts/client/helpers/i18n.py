# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/i18n.py
import json, logging, types
from encodings import utf_8
from frameworks import wulf
_logger = logging.getLogger(__name__)

def convert(utf8String):
    try:
        return utf_8.decode(utf8String)[0]
    except Exception as ex:
        _logger.exception(ex)
        _logger.warning('Wrong UTF8 string: %r', utf8String)
        return utf_8.decode('----')[0]


def isValidKey(key):
    return wulf.isTranslatedKeyValid(key)


def doesTextExist(key):
    return wulf.isTranslatedTextExisted(key)


def makeString(key, *args, **kwargs):
    if not key:
        return key
    if args:
        try:
            return wulf.getTranslatedText(key, args)
        except (TypeError, ValueError, KeyError):
            _logger.warning("Arguments do not match string read by key '%r': %r", key, args)
            return key

    elif kwargs:
        try:
            return wulf.getTranslatedText(key, kwargs)
        except (TypeError, ValueError, KeyError):
            _logger.warning("Arguments do not match string read by key '%s': %s", key, kwargs)
            return key

    return wulf.getTranslatedText(key)


def makeStringJSON(key, argsStr):
    try:
        args = json.loads(argsStr)
        if isinstance(args, dict):
            utf8args = {}
            for k, v in args.iteritems():
                utf8args[k.encode('utf-8')] = v.encode('utf-8')

            return makeString(key, **utf8args)
        utf8args = []
        for v in args:
            if isinstance(v, str):
                utf8args.append(v.encode('utf-8'))
            else:
                utf8args.append(v)

        return makeString(key, *tuple(utf8args))
    except Exception as ex:
        _logger.exception(ex)
        _logger.warning('Failed to translate JSON-encoded string to dict or list: %r, %r', key, argsStr)
        return key


def encodeUtf8(string):
    if isinstance(string, types.UnicodeType):
        return string.encode('utf-8', 'ignore')
    return string