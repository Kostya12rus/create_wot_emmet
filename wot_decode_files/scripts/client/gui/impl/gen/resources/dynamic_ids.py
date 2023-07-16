# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/resources/dynamic_ids.py
from gui.impl.gen_utils import DynAccessor

class DynamicIds(DynAccessor):
    __slots__ = ()

    class _dialog_window(DynAccessor):
        __slots__ = ()
        bottom_content = DynAccessor(74943)
        balance_content = DynAccessor(74944)

    dialog_window = _dialog_window()

    class _tooltip(DynAccessor):
        __slots__ = ()
        normal_content = DynAccessor(74945)
        advanced_content = DynAccessor(74946)

    tooltip = _tooltip()

    class _blueprint_screen(DynAccessor):
        __slots__ = ()
        balance_content = DynAccessor(74947)

    blueprint_screen = _blueprint_screen()

    class _crew_books_buy_dialog(DynAccessor):
        __slots__ = ()
        balance_content = DynAccessor(74948)

    crew_books_buy_dialog = _crew_books_buy_dialog()

    class _demo_window(DynAccessor):
        __slots__ = ()
        image_props = DynAccessor(74949)
        bottom_panel = DynAccessor(74950)

    demo_window = _demo_window()