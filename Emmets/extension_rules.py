# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/extension_rules.py
import re, ResMgr
from soft_exception import SoftException
EXTENSION_RULES_FILE = 'scripts/extension_rules.xml'
g_cache = None

class READ_METHOD(object):
    MERGE = 'merge'
    INCLUDE = 'include'


def init():
    global g_cache
    if g_cache is not None:
        return
    else:
        g_cache = {}
        sec = ResMgr.openSection(EXTENSION_RULES_FILE)
        if not sec:
            raise SoftException("Fail to read '%s'" % EXTENSION_RULES_FILE)
        whitelist = sec['xml_whitelist']
        g_cache['merge_whitelist'] = [ (re.compile(rule['pattern'].asString), rule['type'].asString) for rule in whitelist.values()
                                     ]
        ResMgr.purge(EXTENSION_RULES_FILE, True)
        return


def isExtXML(path):
    path = path.replace('\\', '/')
    if g_cache is None:
        return (False, None)
    else:
        for pattern, method in g_cache.get('merge_whitelist', {}):
            if bool(pattern.match(path)):
                return (True, method)

        return (
         False, None)