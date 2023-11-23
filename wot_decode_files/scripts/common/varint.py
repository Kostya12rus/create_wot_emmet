# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/varint.py
from cStringIO import StringIO as BytesIO

def encode_zigzag64(n):
    return n << 1 ^ n >> 63


def decode_zigzag(n):
    return n >> 1 ^ -(n & 1)


def encode(number):
    buf = BytesIO()
    while True:
        towrite = number & 127
        number >>= 7
        if number:
            buf.write(chr(towrite | 128))
        else:
            buf.write(chr(towrite))
            break

    return buf.getvalue()


def decode_stream(stream):
    shift = 0
    result = 0
    while True:
        i = _read_one(stream)
        result |= (i & 127) << shift
        shift += 7
        if not i & 128:
            return result


def decode_bytes(buf):
    return decode_stream(BytesIO(buf))


def _read_one(stream):
    c = stream.read(1)
    if c == '':
        raise EOFError('Unexpected EOF while reading bytes')
    return ord(c)