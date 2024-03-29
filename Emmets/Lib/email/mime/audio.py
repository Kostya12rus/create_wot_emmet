# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/email/mime/audio.py
__all__ = [
 'MIMEAudio']
import sndhdr
from cStringIO import StringIO
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart
_sndhdr_MIMEmap = {'au': 'basic', 'wav': 'x-wav', 
   'aiff': 'x-aiff', 
   'aifc': 'x-aiff'}

def _whatsnd(data):
    hdr = data[:512]
    fakefile = StringIO(hdr)
    for testfn in sndhdr.tests:
        res = testfn(hdr, fakefile)
        if res is not None:
            return _sndhdr_MIMEmap.get(res[0])

    return


class MIMEAudio(MIMENonMultipart):

    def __init__(self, _audiodata, _subtype=None, _encoder=encoders.encode_base64, **_params):
        if _subtype is None:
            _subtype = _whatsnd(_audiodata)
        if _subtype is None:
            raise TypeError('Could not find audio MIME subtype')
        MIMENonMultipart.__init__(self, 'audio', _subtype, **_params)
        self.set_payload(_audiodata)
        _encoder(self)
        return