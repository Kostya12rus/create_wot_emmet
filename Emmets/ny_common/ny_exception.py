# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/ny_common/ny_exception.py
from soft_exception import SoftException
from items.components.ny_constants import YEARS_INFO

class NYSoftException(SoftException):

    def __init__(self, msg, *args):
        super(NYSoftException, self).__init__()
        self.msg = msg
        self.args = args

    def __str__(self):
        return ('NY{}: {} {}').format(YEARS_INFO.CURRENT_YEAR, self.msg, self.args)