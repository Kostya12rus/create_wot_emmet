# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/xml/etree/ElementInclude.py
import copy
from . import ElementTree
XINCLUDE = '{http://www.w3.org/2001/XInclude}'
XINCLUDE_INCLUDE = XINCLUDE + 'include'
XINCLUDE_FALLBACK = XINCLUDE + 'fallback'

class FatalIncludeError(SyntaxError):
    pass


def default_loader(href, parse, encoding=None):
    with open(href) as (file):
        if parse == 'xml':
            data = ElementTree.parse(file).getroot()
        else:
            data = file.read()
            if encoding:
                data = data.decode(encoding)
    return data


def include(elem, loader=None):
    if loader is None:
        loader = default_loader
    i = 0
    while i < len(elem):
        e = elem[i]
        if e.tag == XINCLUDE_INCLUDE:
            href = e.get('href')
            parse = e.get('parse', 'xml')
            if parse == 'xml':
                node = loader(href, parse)
                if node is None:
                    raise FatalIncludeError('cannot load %r as %r' % (href, parse))
                node = copy.copy(node)
                if e.tail:
                    node.tail = (node.tail or '') + e.tail
                elem[i] = node
            else:
                if parse == 'text':
                    text = loader(href, parse, e.get('encoding'))
                    if text is None:
                        raise FatalIncludeError('cannot load %r as %r' % (href, parse))
                    if i:
                        node = elem[i - 1]
                        node.tail = (node.tail or '') + text + (e.tail or '')
                    else:
                        elem.text = (elem.text or '') + text + (e.tail or '')
                    del elem[i]
                    continue
                else:
                    raise FatalIncludeError('unknown parse type in xi:include tag (%r)' % parse)
        elif e.tag == XINCLUDE_FALLBACK:
            raise FatalIncludeError('xi:fallback tag must be child of xi:include (%r)' % e.tag)
        else:
            include(e, loader)
        i = i + 1

    return