# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/parser.py
__all__ = [
 'Parser', 'HeaderParser']
import warnings
from cStringIO import StringIO
from email.feedparser import FeedParser
from email.message import Message

class Parser:

    def __init__(self, *args, **kws):
        if len(args) >= 1:
            if '_class' in kws:
                raise TypeError("Multiple values for keyword arg '_class'")
            kws['_class'] = args[0]
        if len(args) == 2:
            if 'strict' in kws:
                raise TypeError("Multiple values for keyword arg 'strict'")
            kws['strict'] = args[1]
        if len(args) > 2:
            raise TypeError('Too many arguments')
        if '_class' in kws:
            self._class = kws['_class']
            del kws['_class']
        else:
            self._class = Message
        if 'strict' in kws:
            warnings.warn("'strict' argument is deprecated (and ignored)", DeprecationWarning, 2)
            del kws['strict']
        if kws:
            raise TypeError('Unexpected keyword arguments')

    def parse(self, fp, headersonly=False):
        feedparser = FeedParser(self._class)
        if headersonly:
            feedparser._set_headersonly()
        while True:
            data = fp.read(8192)
            if not data:
                break
            feedparser.feed(data)

        return feedparser.close()

    def parsestr(self, text, headersonly=False):
        return self.parse(StringIO(text), headersonly=headersonly)


class HeaderParser(Parser):

    def parse(self, fp, headersonly=True):
        return Parser.parse(self, fp, True)

    def parsestr(self, text, headersonly=True):
        return Parser.parsestr(self, text, True)