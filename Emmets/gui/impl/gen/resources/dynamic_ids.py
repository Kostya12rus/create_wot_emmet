# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/resources/dynamic_ids.py
from gui.impl.gen_utils import DynAccessor

class DynamicIds(DynAccessor):
    __slots__ = ()

    class _dialog_window(DynAccessor):
        __slots__ = ()
        bottom_content = DynAccessor(66590)
        balance_content = DynAccessor(66591)

    dialog_window = _dialog_window()

    class _tooltip(DynAccessor):
        __slots__ = ()
        normal_content = DynAccessor(66592)
        advanced_content = DynAccessor(66593)

    tooltip = _tooltip()

    class _blueprint_screen(DynAccessor):
        __slots__ = ()
        balance_content = DynAccessor(66594)

    blueprint_screen = _blueprint_screen()

    class _crew_books_buy_dialog(DynAccessor):
        __slots__ = ()
        balance_content = DynAccessor(66595)

    crew_books_buy_dialog = _crew_books_buy_dialog()

    class _prem_dashboard(DynAccessor):
        __slots__ = ()
        header = DynAccessor(66596)
        premium_card = DynAccessor(66597)
        double_xp_card = DynAccessor(66598)
        piggy_bank_card = DynAccessor(66599)
        dog_tags_card = DynAccessor(66600)
        premium_quests_card = DynAccessor(66601)
        maps_black_list_card = DynAccessor(66602)

    prem_dashboard = _prem_dashboard()

    class _demo_window(DynAccessor):
        __slots__ = ()
        image_props = DynAccessor(66603)
        bottom_panel = DynAccessor(66604)

    demo_window = _demo_window()