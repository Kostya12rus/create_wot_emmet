# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-os2emx/_emx_link.py
import os, errno
__all__ = [
 'link']

def link(source, target):
    s = os.open(source, os.O_RDONLY | os.O_BINARY)
    if os.isatty(s):
        raise OSError, (errno.EXDEV, 'Cross-device link')
    data = os.read(s, 1024)
    try:
        t = os.open(target, os.O_WRONLY | os.O_BINARY | os.O_CREAT | os.O_EXCL)
    except OSError:
        os.close(s)
        raise

    try:
        while data:
            os.write(t, data)
            data = os.read(s, 1024)

    except OSError:
        os.close(s)
        os.close(t)
        os.unlink(target)
        raise

    os.close(s)
    os.close(t)


if __name__ == '__main__':
    import sys
    try:
        link(sys.argv[1], sys.argv[2])
    except IndexError:
        print 'Usage: emx_link <source> <target>'
    except OSError:
        print 'emx_link: %s' % str(sys.exc_info()[1])