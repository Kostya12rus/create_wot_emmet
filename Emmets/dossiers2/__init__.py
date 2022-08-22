# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/__init__.py
from dossiers2.common.utils import getDossierVersion
from dossiers2.custom import updaters
from dossiers2.custom.builders import *

def init():
    from dossiers2.custom import init as custom_init
    custom_init()
    from dossiers2.ui import init as ui_init
    ui_init()