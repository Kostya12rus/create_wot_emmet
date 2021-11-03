# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/errors.py


class MessageError(Exception):
    pass


class MessageParseError(MessageError):
    pass


class HeaderParseError(MessageParseError):
    pass


class BoundaryError(MessageParseError):
    pass


class MultipartConversionError(MessageError, TypeError):
    pass


class CharsetError(MessageError):
    pass


class MessageDefect:

    def __init__(self, line=None):
        self.line = line


class NoBoundaryInMultipartDefect(MessageDefect):
    pass


class StartBoundaryNotFoundDefect(MessageDefect):
    pass


class FirstHeaderLineIsContinuationDefect(MessageDefect):
    pass


class MisplacedEnvelopeHeaderDefect(MessageDefect):
    pass


class MalformedHeaderDefect(MessageDefect):
    pass


class MultipartInvariantViolationDefect(MessageDefect):
    pass