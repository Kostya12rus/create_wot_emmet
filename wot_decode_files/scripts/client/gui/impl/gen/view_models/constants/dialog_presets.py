# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/constants/dialog_presets.py
from frameworks.wulf import ViewModel

class DialogPresets(ViewModel):
    __slots__ = ()
    QUIT_GAME = 'quitGame'
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    BLUEPRINTS_CONVERSION = 'blueprintsConversion'
    MAPS_BLACKLIST = 'mapsBlacklist'
    TROPHY_DEVICE_UPGRADE = 'trophyDeviceUpgrade'
    BUY_BATTLE_PASS = 'buyBattlePass'
    CUSTOMIZATION_INSTALL_BOUND = 'customizationInstallBound'
    DEFAULT = 'default'

    def __init__(self, properties=0, commands=0):
        super(DialogPresets, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DialogPresets, self)._initialize()