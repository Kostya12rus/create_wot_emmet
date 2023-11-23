# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/realm_utils.py
import string, ResMgr as rmgr
from constants import CURRENT_REALM, IS_CLIENT, IS_EDITOR

def getRealmFilePath(filepath):
    parts = filepath.split('.')
    return string.join(parts[:-1] + [CURRENT_REALM] + parts[-1:], '.')


class ResMgr(object):

    class __metaclass__(type):

        def __getattr__(self, item):
            if IS_CLIENT:
                return getattr(rmgr, item)
            return getattr(self if item in ('openSection', 'purge') else rmgr, item)

    @staticmethod
    def openSection(filepath, createIfMissing=False):
        section = (IS_EDITOR or rmgr.openSection)(getRealmFilePath(filepath)) if 1 else None
        if section is not None:
            return section
        else:
            return rmgr.openSection(filepath, createIfMissing)

    @staticmethod
    def purge(filepath, recursive=False):
        if not filepath:
            return
        rmgr.purge(filepath, recursive)
        rmgr.purge(getRealmFilePath(filepath), recursive)