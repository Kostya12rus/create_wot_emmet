# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/craftmachine/contexts.py
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class CraftmachineModulesInfoCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.CRAFTMACHINE_MODULES_INFO

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False