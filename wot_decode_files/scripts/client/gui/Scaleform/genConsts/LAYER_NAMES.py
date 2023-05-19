# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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
    HIDDEN_SERVICE_LAYOUT = 'hiddenServiceLayout'
    OVERLAY = 'overlay'
    TOOL_TIPS = 'toolTips'
    WAITING = 'waiting'
    CURSOR = 'cursor'
    LAYER_ORDER = [UNDEFINED, ROOT, HIDDEN_SERVICE_LAYOUT, MARKER, VIEWS, SUBVIEW, TOP_SUB_VIEW, 
     WINDOWS, FULLSCREEN_WINDOWS, SYSTEM_MESSAGES, DIALOGS, OVERLAY, IME, 
     SERVICE_LAYOUT, TOOL_TIPS, CURSOR, WAITING]
    FOCUS_ORDER = [WAITING, SERVICE_LAYOUT, OVERLAY, DIALOGS, FULLSCREEN_WINDOWS, WINDOWS, 
     TOP_SUB_VIEW, SUBVIEW, VIEWS, MARKER]