# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/DestructibleStickers.py
import BigWorld, math_utils, VehicleStickers

class DestructibleStickers(object):

    def __init__(self, spaceID, model, nodeToAttach):
        self.__model = model
        self.__stickerModel = BigWorld.WGStickerModel(spaceID)
        self.__stickerModel.setLODDistance(1000.0)
        self.__stickerModel.setupSuperModel(model, math_utils.createIdentityMatrix())
        self.__nodeToAttach = nodeToAttach
        nodeToAttach.attach(self.__stickerModel)
        self.__damageStickers = {}

    def destroy(self):
        if self.__model is None:
            return
        else:
            if self.__stickerModel.attached and self.__nodeToAttach is not None:
                self.__nodeToAttach.detach(self.__stickerModel)
            self.__stickerModel.clear()
            self.__damageStickers.clear()
            return

    def addDamageSticker(self, code, stickerID, segStart, segEnd):
        if code in self.__damageStickers:
            return
        else:
            if self.__stickerModel is None:
                return
            handle = self.__stickerModel.addDamageSticker(stickerID, segStart, segEnd)
            self.__damageStickers[code] = VehicleStickers.DamageSticker(stickerID, segStart, segEnd, handle)
            return

    def delDamageSticker(self, code):
        if self.__stickerModel is None:
            return
        else:
            damageSticker = self.__damageStickers.get(code)
            if damageSticker is not None:
                if damageSticker.handle is not None:
                    self.__stickerModel.delSticker(damageSticker.handle)
                del self.__damageStickers[code]
            return