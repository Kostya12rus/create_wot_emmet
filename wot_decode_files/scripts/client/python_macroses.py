# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/python_macroses.py
import ResMgr
from debug_utils import LOG_ERROR
_MACROSES_XML = 'scripts/python_macroses.xml'
g_macroses = {}

def init():
    global g_macroses
    section = ResMgr.openSection(_MACROSES_XML)
    if section is not None:
        for macros in section.values():
            command = macros['id'].asString
            if command in g_macroses:
                LOG_ERROR(('Command "{}" duplicated in python_macroses.xml. Also check in extensions').format(command))
            else:
                g_macroses[command] = macros.asString

    return