# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/encodings/utf_32_be.py
import codecs
encode = codecs.utf_32_be_encode

def decode(input, errors='strict'):
    return codecs.utf_32_be_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.utf_32_be_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_32_be_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_32_be_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_32_be_decode


def getregentry():
    return codecs.CodecInfo(name='utf-32-be', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)