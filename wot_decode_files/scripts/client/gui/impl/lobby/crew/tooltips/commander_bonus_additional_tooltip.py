# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/commander_bonus_additional_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_additional_tooltip_model import CrewPerksAdditionalTooltipModel
from gui.impl.pub import ViewImpl
from items.components.skills_constants import SkillTypeName
ANIMATION_NAME = 'skillCommanderBonus'

class CommanderBonusAdditionalTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.crew.tooltips.CrewPerksAdditionalTooltip())
        settings.model = CrewPerksAdditionalTooltipModel()
        super(CommanderBonusAdditionalTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CommanderBonusAdditionalTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CommanderBonusAdditionalTooltip, self)._onLoading(*args, **kwargs)
        self._fillModel()

    def _fillModel(self):
        with self.viewModel.transaction() as (vm):
            vm.setIcon(backport.image(R.images.gui.maps.icons.tankmen.skills.big.commander_bonus()))
            vm.setTitle(backport.text(R.strings.tooltips.commanderBonus.name()))
            vm.setSkillType(SkillTypeName.COMMANDER_SPECIAL)
            vm.setDescription(backport.text(R.strings.tooltips.commanderBonus.alt.description()))
            vm.setAnimationName(ANIMATION_NAME)
            vm.setInfo(backport.text(R.strings.tooltips.commanderBonus.alt.info()))