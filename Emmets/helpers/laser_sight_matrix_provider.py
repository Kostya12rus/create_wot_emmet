# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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