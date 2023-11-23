# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/encodings/undefined.py
import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        raise UnicodeError('undefined encoding')

    def decode(self, input, errors='strict'):
        raise UnicodeError('undefined encoding')


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        raise UnicodeError('undefined encoding')


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        raise UnicodeError('undefined encoding')


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='undefined', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)