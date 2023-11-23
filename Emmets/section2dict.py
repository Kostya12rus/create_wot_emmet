# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/section2dict.py
import typing
if typing.TYPE_CHECKING:
    from ResMgr import DataSection

def _parseDataSection(dataSection):
    if not len(dataSection.values()):
        return _normalizeValue(dataSection.asString)
    result = {}
    for section in dataSection.values():
        key = section.name
        value = _parseDataSection(section)
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [
                 result[key], value]
        else:
            result[key] = value

    return result


def _normalizeValue(value):
    if value.isdigit():
        value = int(value)
    else:
        try:
            value = float(value)
        except ValueError:
            pass

    return value


def parse(data):
    if not len(data.values()):
        return {}
    return _parseDataSection(data)