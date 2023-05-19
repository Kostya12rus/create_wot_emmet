# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/demount_kit/demount_kit_utils.py
import typing
from gui.impl import backport
from gui.impl.gen import R
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.artefacts import OptionalDevice

def getDemountDialogTitle(item, forFitting=False, fromSlot=False):
    titleRes = R.strings.demount_kit.equipmentDemountFromSlot if fromSlot else R.strings.demount_kit.equipmentDemount
    titleRes = titleRes.confirmationForFitting.title if forFitting else titleRes.confirmation.title
    return backport.text(titleRes(), equipment=item.userName)