# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/platoon/view/slot_label_html_handler.py
import json
from HTMLParser import HTMLParser
from gui.impl.gen.view_models.views.lobby.platoon.slot_label_element_model import Types

def getStyle(attrs):
    result = {}
    if attrs.get('width'):
        result['width'] = ('{}rem').format(attrs.get('width'))
    if attrs.get('height'):
        result['height'] = ('{}rem').format(attrs.get('height'))
    if attrs.get('vspace'):
        result['marginTop'] = ('{}rem').format(attrs.get('vspace'))
        result['marginBottom'] = ('{}rem').format(attrs.get('vspace'))
    if attrs.get('hspace'):
        result['marginLeft'] = ('{}rem').format(attrs.get('hspace'))
        result['marginRight'] = ('{}rem').format(attrs.get('hspace'))
    if attrs.get('src'):
        result['background'] = ('url({}) center / contain no-repeat').format(attrs.get('src'))
    if attrs.get('size'):
        result['fontSize'] = ('{}rem').format(attrs.get('size'))
    if attrs.get('color'):
        result['color'] = attrs.get('color')
    return json.dumps(result)


class SlotLabelHtmlParser(HTMLParser, object):

    def __init__(self):
        super(SlotLabelHtmlParser, self).__init__()
        self.parsingResult = []

    def handle_starttag(self, tag, attrs):
        self.parsingResult.append({'tag': tag, 'attrs': self.__attrsToDict(attrs)})

    def handle_data(self, data):
        self.parsingResult.append({'tag': '', 'data': data})

    def getElements(self):
        result = []
        for index, entry in enumerate(self.parsingResult):
            entryTag = entry.get('tag')
            if entryTag == 'img':
                result.append({'type': Types.IMAGE, 'style': getStyle(entry.get('attrs'))})
            elif entryTag == 'br':
                result.append({'type': Types.TEXT, 'text': '\n'})
            elif entryTag == '':
                data = entry.get('data')
                if data == ' ':
                    continue
                data = {'type': Types.TEXT, 'text': data}
                if index > 0 and self.parsingResult[index - 1].get('tag') == 'font':
                    data['style'] = getStyle(self.parsingResult[index - 1].get('attrs'))
                result.append(data)

        return result

    @staticmethod
    def __attrsToDict(attrs):
        return {parameter: value for parameter, value in attrs}