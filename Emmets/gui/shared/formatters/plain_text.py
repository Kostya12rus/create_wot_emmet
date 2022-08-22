# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/plain_text.py
from gui.server_events.cond_formatters import FORMATTER_IDS
from gui.server_events import formatters
from gui.shared.formatters import text_styles

def getDefaultPlainTextFormatters():
    return {FORMATTER_IDS.SIMPLE_TITLE: formatters.titleFormatPlain, 
       FORMATTER_IDS.CUMULATIVE: formatters.titleCumulativeFormatPlain, 
       FORMATTER_IDS.COMPLEX: formatters.titleComplexFormatPlain, 
       FORMATTER_IDS.RELATION: formatters.titleRelationFormatPlain, 
       FORMATTER_IDS.DESCRIPTION: text_styles.highlightTextPlain, 
       FORMATTER_IDS.COMPLEX_RELATION: formatters.titleComplexRelationFormatPlain}


class PlainTextFormatter(object):
    _formatters = getDefaultPlainTextFormatters()

    @classmethod
    def getPlainTextFromFormattedField(cls, formattableField):
        formatterName = formattableField.formatterID
        formatter = cls._formatters.get(formatterName)
        text = formatter(*formattableField.args)
        return text