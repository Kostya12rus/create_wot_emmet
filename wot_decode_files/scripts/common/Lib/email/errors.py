# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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