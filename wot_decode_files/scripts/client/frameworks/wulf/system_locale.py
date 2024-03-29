# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/system_locale.py
import typing
from .gui_constants import NumberFormatType, RealFormatType
from .gui_constants import TimeFormatType, DateFormatType
from .py_object_binder import PyObjectEntity

class SystemLocale(PyObjectEntity):

    @classmethod
    def create(cls, proxy):
        locale_ = SystemLocale()
        locale_.bind(proxy)
        return locale_

    def destroy(self):
        self.unbind()

    def getNumberFormat(self, value, formatType=NumberFormatType.INTEGRAL):
        return self.proxy.getNumberFormat(int(value), formatType)

    def getRealFormat(self, value, formatType=RealFormatType.FRACTIONAL):
        return self.proxy.getRealFormat(value, formatType)

    def getTimeFormat(self, value, formatType=TimeFormatType.SHORT_FORMAT):
        return self.proxy.getTimeFormat(value, formatType)

    def getDateFormat(self, value, formatType=DateFormatType.SHORT_FORMAT):
        return self.proxy.getDateFormat(value, formatType)

    def caseMap(self, value, caseType):
        return self.proxy.caseMap(value, caseType)