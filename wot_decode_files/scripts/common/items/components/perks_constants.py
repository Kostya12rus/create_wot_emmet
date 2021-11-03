# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/perks_constants.py
PERKS_XML_FILE = 'perks.xml'

class PERKS_TYPE:
    SIMPLE = 1
    ULTIMATE = 2
    ANY = SIMPLE | ULTIMATE
    CONFIGURATION_MAPPING = {True: ULTIMATE, 
       False: SIMPLE}