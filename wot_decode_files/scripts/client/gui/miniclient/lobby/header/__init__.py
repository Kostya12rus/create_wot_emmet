# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/header/__init__.py
import create_squad as _create_squad, fight_button_ as _fight_button
from battle_type_selector import configure_pointcuts as _configure_selector_pointcuts

def configure_pointcuts(config):
    _configure_selector_pointcuts()
    _create_squad.OnCreateSquadClickPointcut()
    _fight_button.DisableFightButtonPointcut(config)