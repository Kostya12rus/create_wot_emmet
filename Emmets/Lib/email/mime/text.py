# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/mime/text.py
__all__ = [
 'MIMEText']
from email.encoders import encode_7or8bit
from email.mime.nonmultipart import MIMENonMultipart

class MIMEText(MIMENonMultipart):

    def __init__(self, _text, _subtype='plain', _charset='us-ascii'):
        MIMENonMultipart.__init__(self, 'text', _subtype, **{'charset': _charset})
        self.set_payload(_text, _charset)