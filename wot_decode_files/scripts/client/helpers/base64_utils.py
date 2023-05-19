# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/base64_utils.py
import base64

def base64UrlDecode(encodedValue):
    if isinstance(encodedValue, unicode):
        encodedValue = encodedValue.encode('ascii')
    rem = len(encodedValue) % 4
    if rem > 0:
        encodedValue += '=' * (4 - rem)
    return base64.urlsafe_b64decode(encodedValue)