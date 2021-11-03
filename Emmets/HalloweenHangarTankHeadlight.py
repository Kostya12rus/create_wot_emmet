# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/HalloweenHangarTankHeadlight.py
import BigWorld, AnimationSequence
from gui.shared.utils.graphics import isRendererPipelineDeferred
_isDeferredRenderer = isRendererPipelineDeferred()

class HalloweenHangarTankHeadlight(BigWorld.Entity):

    def __init__(self):
        super(HalloweenHangarTankHeadlight, self).__init__()
        self.model = None
        self.animator = None
        return

    def prerequisites(self):
        if not self.modelName:
            return []
        result = [self.modelName]
        if self.animationSequence:
            result.append(AnimationSequence.Loader(self.animationSequence, self.spaceID))
        return result

    def onEnterWorld(self, prereqs):
        if not self.modelName or self.modelName in prereqs.failedIDs:
            return
        model = prereqs[self.modelName]
        self.model = model
        self.filter = BigWorld.DumbFilter()
        self.model.addMotor(BigWorld.Servo(self.matrix))
        if not self.animationSequence or self.animationSequence in prereqs.failedIDs:
            return
        self.animator = prereqs[self.animationSequence]
        self.animator.bindTo(AnimationSequence.ModelWrapperContainer(self.model, self.spaceID))
        self.animator.start()
        if hasattr(self.animator, 'setBoolParam'):
            self.animator.setBoolParam('isDeferred', _isDeferredRenderer)

    def onLeaveWorld(self):
        if self.animator is not None:
            self.animator.stop()
            self.animator = None
        return