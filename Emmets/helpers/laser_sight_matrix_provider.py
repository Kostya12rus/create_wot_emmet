# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/laser_sight_matrix_provider.py
import Math

class LaserSightMatrixProvider(object):
    __slots__ = ('__beamLength', '__beamMatrix')

    def __init__(self):
        super(LaserSightMatrixProvider, self).__init__()
        self.__beamLength = 0.0
        self.__beamMatrix = Math.MatrixProduct()
        self.__beamMatrix.a = Math.Matrix()
        self.__beamMatrix.b = Math.Matrix()

    @property
    def beamMatrix(self):
        return self.__beamMatrix

    @beamMatrix.setter
    def beamMatrix(self, matrix):
        self.__beamMatrix.a.setScale((1.0, 1.0, self.__beamLength))
        self.__beamMatrix.b = matrix

    @property
    def beamLength(self):
        return self.__beamLength

    @beamLength.setter
    def beamLength(self, length):
        self.__beamLength = length
        self.__beamMatrix.a.setScale((1.0, 1.0, self.__beamLength))