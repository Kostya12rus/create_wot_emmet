# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/battle_pass/carousel_data_provider.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import HangarCarouselDataProvider
from gui.shared.formatters import text_styles
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController

class BattlePassCarouselDataProvider(HangarCarouselDataProvider):
    battlePassController = dependency.descriptor(IBattlePassController)

    def _buildVehicle(self, vehicle):

        def formatSpecialVehPoints(value):
            return text_styles.makeHtmlString('html_templates:lobby/tank_carousel', 'specialVehPoints', ctx={'value': value})

        result = super(BattlePassCarouselDataProvider, self)._buildVehicle(vehicle)
        if not self._isSuitableForQueue(vehicle) or not self.battlePassController.isVisible():
            return result
        currentPoints, limitPoints = self.battlePassController.getVehicleProgression(vehicle.intCD)
        isSpecialVehicle = self.battlePassController.isSpecialVehicle(vehicle.intCD)
        result['hasProgression'] = limitPoints > 0
        if limitPoints > 0:
            limitReached = currentPoints >= limitPoints
            pointsFormatter = formatSpecialVehPoints if isSpecialVehicle and limitReached else text_styles.counterLabelText
            limitFormatter = formatSpecialVehPoints if isSpecialVehicle else text_styles.counterLabelText
            limitPointsFormatted = limitFormatter((' / {}').format(limitPoints))
            result['progressionPoints'] = {'currentPoints': pointsFormatter(currentPoints), 
               'limitPoints': limitPointsFormatted, 
               'limitReached': limitReached, 
               'isSpecialVehicle': isSpecialVehicle}
        return result