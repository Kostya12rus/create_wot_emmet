# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/complex_formatters.py
from gui import makeHtmlString
from gui.shared.utils.functions import stripColorTagDescrTags
from helpers import i18n
_TEXT_FORMAT = "{0[0]}{1}{0[1]}\n<font size='1' > </font>\n"
_TOOLTIP_KIND = ('header', 'body', 'note', 'attention')
_BLOCK_TAGS_MAP = {'HEADER': {'INFO': (
                     makeHtmlString('html_templates:lobby/tooltips_complex', 'header_info_start'),
                     makeHtmlString('html_templates:lobby/tooltips_complex', 'header_info_end')), 
              'WARNING': (
                        makeHtmlString('html_templates:lobby/tooltips_complex', 'header_warning_start'),
                        makeHtmlString('html_templates:lobby/tooltips_complex', 'header_warning_end'))}, 
   'BODY': {'INFO': (
                   makeHtmlString('html_templates:lobby/tooltips_complex', 'body_info_start'),
                   makeHtmlString('html_templates:lobby/tooltips_complex', 'body_info_end')), 
            'WARNING': (
                      makeHtmlString('html_templates:lobby/tooltips_complex', 'body_warning_start'),
                      makeHtmlString('html_templates:lobby/tooltips_complex', 'body_warning_end'))}, 
   'NOTE': {'INFO': (
                   makeHtmlString('html_templates:lobby/tooltips_complex', 'note_info_start'),
                   makeHtmlString('html_templates:lobby/tooltips_complex', 'note_info_end')), 
            'WARNING': [
                      makeHtmlString('html_templates:lobby/tooltips_complex', 'note_warning_start'),
                      makeHtmlString('html_templates:lobby/tooltips_complex', 'note_warning_end')]}, 
   'ATTENTION': {'INFO': (
                        makeHtmlString('html_templates:lobby/tooltips_complex', 'attention_info_start'),
                        makeHtmlString('html_templates:lobby/tooltips_complex', 'attention_info_end')), 
                 'WARNING': (
                           makeHtmlString('html_templates:lobby/tooltips_complex', 'attention_warning_start'),
                           makeHtmlString('html_templates:lobby/tooltips_complex', 'attention_warning_end'))}}

def _getTags(blockType, formatType):
    blockTag = _BLOCK_TAGS_MAP[blockType]
    if formatType in blockTag:
        return blockTag[formatType]
    return ('', '')


def _getFormattedText(text, blockType, formatType):
    if formatType is None:
        formatType = 'INFO'
    tags = _getTags(blockType, formatType)
    return _TEXT_FORMAT.format(tags, text)


def _doFormatToolTipFromKey(tooltipID, formatType):
    result = []
    for kind in _TOOLTIP_KIND:
        contentKey = ('{}/{}').format(tooltipID, kind)
        content = i18n.makeString(contentKey)
        subkey = contentKey[1:].split(':', 1)
        if content and subkey and content != subkey[1]:
            result.append(_getFormattedText(content, kind.upper(), formatType))

    return ('').join(result)


def _doFormatToolTipFromText(tooltipID, formatType):
    result = ''
    for tooltipKind in _TOOLTIP_KIND:
        tooltipBlock = tooltipKind.upper()
        tags = {'open': '{' + tooltipBlock + '}', 
           'close': '{/' + tooltipBlock + '}'}
        indicies = {'start': tooltipID.find(tags['open']), 
           'end': tooltipID.find(tags['close'])}
        if indicies['start'] != -1 and indicies['end'] != -1:
            indicies['start'] += len(tags['open'])
            result += _getFormattedText(stripColorTagDescrTags(tooltipID[indicies['start']:indicies['end']]), tooltipBlock, formatType)

    return result


def doFormatData(data, formatType):
    result = []
    for kind in _TOOLTIP_KIND:
        if kind in data and data[kind] is not None:
            result.append(_getFormattedText(data[kind], kind.upper(), formatType))

    return ('').join(result)


def doFormatToolTip(tooltipID, formatType):
    if not tooltipID:
        return ''
    if tooltipID.startswith('#'):
        return _doFormatToolTipFromKey(tooltipID, formatType)
    return _doFormatToolTipFromText(tooltipID, formatType)