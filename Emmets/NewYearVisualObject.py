# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/NewYearVisualObject.py
import logging, BigWorld, math_utils
_logger = logging.getLogger(__name__)

class NewYearVisualObject(BigWorld.Entity):

    def __init__(self):
        BigWorld.Entity.__init__(self)
        self.model = None
        self.scaleMatrix = math_utils.createSRTMatrix(self.scale, (0, 0, 0), (0, 0,
                                                                              0))
        return

    def prerequisites(self):
        if not self.modelName:
            return []
        return [self.modelName]

    def onEnterWorld(self, prereqs):
        if not self.modelName:
            return
        if self.modelName in prereqs.failedIDs:
            _logger.error('Failed to load model "%s"', self.modelName)
            return
        model = prereqs[self.modelName]
        model.castsShadow = False
        self.model = model
        self.filter = BigWorld.DumbFilter()
        resultMatrix = math_utils.MatrixProviders.product(self.scaleMatrix, self.matrix)
        self.model.addMotor(BigWorld.Servo(resultMatrix))

    def onLeaveWorld(self):
        pass