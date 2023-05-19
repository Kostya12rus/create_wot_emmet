# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCVehicleMessages.py
from gui.Scaleform.daapi.view.battle.shared import messages
_VEHICLE_MESSAGES_FILE = 'bc_vehicle_messages_panel.xml'

class BCVehicleMessages(messages.VehicleMessages):

    def __init__(self):
        super(BCVehicleMessages, self).__init__()
        self.setSettingFile(_VEHICLE_MESSAGES_FILE)