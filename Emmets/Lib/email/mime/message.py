# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/mime/message.py
__all__ = [
 'MIMEMessage']
from email import message
from email.mime.nonmultipart import MIMENonMultipart

class MIMEMessage(MIMENonMultipart):

    def __init__(self, _msg, _subtype='rfc822'):
        MIMENonMultipart.__init__(self, 'message', _subtype)
        if not isinstance(_msg, message.Message):
            raise TypeError('Argument is not an instance of Message')
        message.Message.attach(self, _msg)
        self.set_default_type('message/rfc822')