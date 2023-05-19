# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/doc_loaders/hints_layout.py
import resource_helper
from gui.shared.formatters import text_styles

def getLayout(layoutName):
    global _hintsLayout
    if _hintsLayout is None:
        _hintsLayout = _readHintsLayouts()
    return _hintsLayout.get(layoutName, None)


_HINTS_LAYOUT_FILE_PATH = 'gui/hints_layout.xml'

def _convertHints(hintsList):
    return [ setattr(hint, 'hintText', text_styles.tutorial(hint.get('hintText', ''))) for hint in hintsList ]


def _readHintsLayouts():
    result = {}
    ctx, section = resource_helper.getRoot(_HINTS_LAYOUT_FILE_PATH)
    for ctx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(ctx, subSection, name='layout')
        if item.name == 'hints':
            value = _convertHints(item.value)
        else:
            value = item.value
        value['hintID'] = item.name
        result[item.name] = value

    return result


_hintsLayout = None