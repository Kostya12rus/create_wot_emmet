# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/ui/__init__.py
from dossiers2.ui.layouts import init as ui_layouts_init
from dossiers2.ui.achievements import init as achieves_init

def init():
    achieves_init('scripts/item_defs/achievements.xml')
    ui_layouts_init()