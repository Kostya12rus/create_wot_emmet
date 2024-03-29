# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/sunaudio.py
from warnings import warnpy3k
warnpy3k('the sunaudio module has been removed in Python 3.0; use the sunau module instead', stacklevel=2)
del warnpy3k
MAGIC = '.snd'

class error(Exception):
    pass


def get_long_be(s):
    return ord(s[0]) << 24 | ord(s[1]) << 16 | ord(s[2]) << 8 | ord(s[3])


def gethdr(fp):
    if fp.read(4) != MAGIC:
        raise error, 'gethdr: bad magic word'
    hdr_size = get_long_be(fp.read(4))
    data_size = get_long_be(fp.read(4))
    encoding = get_long_be(fp.read(4))
    sample_rate = get_long_be(fp.read(4))
    channels = get_long_be(fp.read(4))
    excess = hdr_size - 24
    if excess < 0:
        raise error, 'gethdr: bad hdr_size'
    if excess > 0:
        info = fp.read(excess)
    else:
        info = ''
    return (
     data_size, encoding, sample_rate, channels, info)


def printhdr(file):
    hdr = gethdr(open(file, 'r'))
    data_size, encoding, sample_rate, channels, info = hdr
    while info[-1:] == '\x00':
        info = info[:-1]

    print 'File name:  ', file
    print 'Data size:  ', data_size
    print 'Encoding:   ', encoding
    print 'Sample rate:', sample_rate
    print 'Channels:   ', channels
    print 'Info:       ', repr(info)