# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/crew_perks_tooltip.py
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_tooltip_booster_model import CrewPerksTooltipBoosterModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_tooltip_model import CrewPerksTooltipModel
from gui.impl.pub import ViewImpl
from gui.shared.gui_items.Tankman import getTankmanSkill, crewMemberRealSkillLevel, tankmanPersonalSkillLevel, getBattleBooster
from gui.shared.skill_parameters.skills_packers import g_skillPackers, packBase
from gui.shared.tooltips.advanced import SKILL_MOVIES
from helpers import dependency
from items.tankmen import getSkillsConfig, MAX_SKILL_LEVEL, SEPARATE_SKILLS
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Tankman import Tankman, TankmanSkill
    from items.readers.skills_readers import SkillDescrsArg
    from gui.shared.gui_items.Vehicle import Vehicle

class CrewPerksTooltip(ViewImpl):
    _itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = ('_skillName', '_tankman', '_tankmanVehicle', '_skill', '_descrArgs',
                 '_skillLevel', '_skillBooster', '_isCommonExtraAvailable')

    def __init__(self, skillName, tankmanId, skillLevel=None, isCommonExtraAvailable=False):
        settings = ViewSettings(R.views.lobby.crew.tooltips.CrewPerksTooltip())
        settings.model = CrewPerksTooltipModel()
        self._skillName = skillName
        self._isCommonExtraAvailable = isCommonExtraAvailable
        self._tankman = self._itemsCache.items.getTankman(int(tankmanId)) if tankmanId else None
        self._tankmanVehicle = self._getVehicle()
        self._skillBooster = getBattleBooster(self._tankmanVehicle, self._skillName)
        self._skill = getTankmanSkill(skillName, tankman=self._tankman)
        self._descrArgs = getSkillsConfig().getSkill(skillName).uiSettings.descrArgs
        self._skillLevel = self._getSkillLevel(skillLevel)
        super(CrewPerksTooltip, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(CrewPerksTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CrewPerksTooltip, self)._onLoading(*args, **kwargs)
        self._fillModel()

    def _getVehicle(self):
        if self._tankman is None:
            return
        else:
            if self._tankman.isInTank:
                return self._itemsCache.items.getVehicle(self._tankman.vehicleInvID)
            return

    def _getSkillLevel(self, skillLevel=None):
        if skillLevel is not None:
            return skillLevel
        else:
            if not self._skill.isAlreadyEarned:
                return 0
            if self._tankman:
                if not self._tankman.isInTank or self._skillName in SEPARATE_SKILLS:
                    return tankmanPersonalSkillLevel(self._tankman, self._skillName, self._skillBooster)
                return crewMemberRealSkillLevel(self._tankmanVehicle, self._skill.name, self._tankman.role, True)
            return 0

    def _fillModel(self):
        with self.viewModel.transaction() as (vm):
            vm.setIcon(self._skill.bigIconPath)
            vm.setTitle(self._skill.userName)
            vm.setLevel(self._skillLevel)
            vm.setSkillType(self._skill.typeName)
            vm.setIsCommonExtraAvailable(self._isCommonExtraAvailable)
            vm.setIsAdvancedTooltipEnable(bool(SKILL_MOVIES.get(self._skill.name, None)))
            if self._skillLevel > 0:
                self.fillCurrentLvlInfo(vm)
            else:
                vm.setDescription(self._skill.getMaxLvlDescription())
        return

    def fillCurrentLvlInfo(self, vm):
        boosters = vm.getBoosters()
        boosters.clear()
        skillPacker = g_skillPackers.get(self._skillName, packBase)
        skillParams = skillPacker(self._descrArgs, self._skillLevel, dict((name,
         (lambda b=self._skillBooster, n=name: b if b and hasattr(b, n) else None)) for name, _ in self._descrArgs) if self._skillName in g_skillPackers else None)
        keyArgs = skillParams.get('keyArgs', {})
        if self._skillLevel < MAX_SKILL_LEVEL:
            kpiArgs = skillParams.get('kpiArgs', [])
            for kpiValue, kpiText, impact in kpiArgs:
                booster = CrewPerksTooltipBoosterModel()
                booster.setValue(kpiValue)
                booster.setText(kpiText)
                booster.setImpact(impact)
                boosters.addViewModel(booster)

        vm.setDescription(self._skill.currentLvlDescription % keyArgs)
        return