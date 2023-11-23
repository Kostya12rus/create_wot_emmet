# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/FilterUtilities.py
import BigWorld

def enableVisualiseAvatarFilter(entity):
    if hasattr(entity.filter, 'debugMatrixes') and callable(entity.filter.debugMatrixes):
        disableVisualiseAvatarFilter(entity)
        entity._filterCubeModels = []
        for matrixProvider in entity.filter.debugMatrixes():
            cubeModel = BigWorld.Model('helpers/models/unit_cube.model')
            servo = BigWorld.Servo(matrixProvider)
            cubeModel.addMotor(servo)
            entity.addModel(cubeModel)
            entity._filterCubeModels.append(cubeModel)


def disableVisualiseAvatarFilter(entity):
    if hasattr(entity, '_filterCubeModels'):
        for cube in entity._filterCubeModels:
            entity.delModel(cube)

        del entity._filterCubeModels


def enableVisualiseAllAvatarFilters():
    for entity in BigWorld.entities.values():
        enableVisualiseAvatarFilter(entity)


def disableVisualiseAllAvatarFilters():
    for entity in BigWorld.entities.values():
        disableVisualiseAvatarFilter(entity)