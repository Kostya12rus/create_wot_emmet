# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/mime/text.py
__all__ = [
 'MIMEText']
from email.encoders import encode_7or8bit
from email.mime.nonmultipart import MIMENonMultipart

class MIMEText(MIMENonMultipart):

    def __init__(self, _text, _subtype='plain', _charset='us-ascii'):
        MIMENonMultipart.__init__(self, 'text', _subtype, **{'charset': _charset})
        self.set_payload(_text, _charset)