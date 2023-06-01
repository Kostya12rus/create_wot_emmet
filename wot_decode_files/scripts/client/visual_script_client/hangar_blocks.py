# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/hangar_blocks.py
from visual_script import ASPECT
from visual_script.block import Block, Meta
from visual_script.dependency import dependencyImporter
from visual_script.slot_types import SLOT_TYPE
utils, dependency, CGF, hangar_camera_manager = dependencyImporter('skeletons.gui.shared.utils', 'helpers.dependency', 'CGF', 'cgf_components.hangar_camera_manager')

class HangarCameraMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 6750207

    @classmethod
    def blockCategory(cls):
        return 'Camera'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/camera'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class GetCamera(Block, HangarCameraMeta):
    hangarSpace = dependency.descriptor(utils.IHangarSpace)

    def __init__(self, *args, **kwargs):
        super(GetCamera, self).__init__(*args, **kwargs)
        self._position = self._makeDataOutputSlot('position', SLOT_TYPE.VECTOR3, self._getPosition)
        self._direction = self._makeDataOutputSlot('direction', SLOT_TYPE.VECTOR3, self._getDirection)

    def _getPosition(self):
        cameraManager = CGF.getManager(self.hangarSpace.spaceID, hangar_camera_manager.HangarCameraManager)
        if cameraManager:
            self._position.setValue(cameraManager.getCurrentCameraPosition())

    def _getDirection(self):
        cameraManager = CGF.getManager(self.hangarSpace.spaceID, hangar_camera_manager.HangarCameraManager)
        if cameraManager:
            self._direction.setValue(cameraManager.getCurrentCameraDirection())