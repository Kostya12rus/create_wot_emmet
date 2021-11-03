# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/LAYER_NAMES.py


class LAYER_NAMES(object):
    UNDEFINED = ''
    ROOT = 'root'
    MARKER = 'marker'
    VIEWS = 'view'
    SUBVIEW = 'subView'
    TOP_SUB_VIEW = 'topSubView'
    WINDOWS = 'window'
    FULLSCREEN_WINDOWS = 'fullscreenWindow'
    IME = 'ime'
    SYSTEM_MESSAGES = 'systemMessages'
    DIALOGS = 'topWindow'
    SERVICE_LAYOUT = 'serviceLayout'
    OVERLAY = 'overlay'
    TOOL_TIPS = 'toolTips'
    WAITING = 'waiting'
    CURSOR = 'cursor'
    LAYER_ORDER = [UNDEFINED, ROOT, MARKER, VIEWS, SUBVIEW, TOP_SUB_VIEW, WINDOWS, FULLSCREEN_WINDOWS, SYSTEM_MESSAGES, DIALOGS, OVERLAY, IME, SERVICE_LAYOUT, TOOL_TIPS, CURSOR, WAITING]
    FOCUS_ORDER = [WAITING, SERVICE_LAYOUT, OVERLAY, DIALOGS, FULLSCREEN_WINDOWS, WINDOWS, TOP_SUB_VIEW, SUBVIEW, VIEWS, MARKER]