# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/profile/aspects.py
from gui.Scaleform.locale.MINICLIENT import MINICLIENT
from gui.shared.utils.functions import makeTooltip
from helpers import aop

class MakeClanBtnUnavailable(aop.Aspect):

    def __init__(self, config=None):
        self.__config = config or {}
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_return_value['btnEnabled'] = False
        original_return_value['btnTooltip'] = makeTooltip(None, None, None, self.__config.get('sandbox_platform_message', MINICLIENT.ACCOUNTPOPOVER_WARNING))
        return original_return_value


class MakeClubProfileButtonUnavailable(aop.Aspect):

    def atCall(self, cd):
        cd.change()
        return (
         [
          False], {})