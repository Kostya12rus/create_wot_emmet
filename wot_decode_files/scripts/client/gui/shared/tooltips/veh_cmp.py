# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/veh_cmp.py
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.shared.formatters import text_styles, icons
from gui.shared.gui_items.Tankman import getSkillSmallIconPath, getRoleWhiteIconPath, Tankman
from gui.shared.tooltips import TOOLTIP_TYPE, formatters
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache
from gui.impl import backport
from gui.impl.gen import R

class VehCmpCustomizationTooltip(BlocksTooltipData):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, context):
        super(VehCmpCustomizationTooltip, self).__init__(context, TOOLTIP_TYPE.VEH_CMP_CUSTOMIZATION)
        self._setContentMargin(top=20, left=20, bottom=20, right=20)
        self._setWidth(420)
        self.__vehicle = None
        self.__camo = None
        self._customCamo = False
        return

    def _packBlocks(self, *args):
        self._customCamo = args[0]
        self.__vehicle = cmp_helpers.getCmpConfiguratorMainView().getCurrentVehicle()
        self.__camo = cmp_helpers.getSuitableCamouflage(self.__vehicle)
        camouflage = self.__vehicle.getBonusCamo()
        if camouflage is not None and not self.__camo:
            self.__camo = self.itemsCache.items.getItemByCD(camouflage.compactDescr)
            self._customCamo = False
        items = [self.__packTitleBlock(),
         self.__packBonusBlock(),
         self.__packBottomPanelBlock()]
        return items

    def __packTitleBlock(self):
        blocks = [
         formatters.packTextBlockData(text=text_styles.highTitle(backport.text(R.strings.veh_compare.vehConf.tooltips.camoTitle())), padding=formatters.packPadding(top=-3, left=-2)),
         formatters.packImageBlockData(img=self.__camo.bonus.iconBig, padding=formatters.packPadding(top=-6, left=90))]
        return formatters.packBuildUpBlockData(blocks)

    def __packBonusBlock(self):
        blocks = [
         formatters.packTextParameterBlockData(name=self.__camo.bonus.description, value=text_styles.bonusAppliedText(('+{}').format(self.__camo.bonus.getFormattedValue(self.__vehicle))), valueWidth=53, gap=18, padding=formatters.packPadding(top=-5, bottom=-7))]
        return formatters.packBuildUpBlockData(blocks, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE)

    def __packBottomPanelBlock(self):
        title = R.strings.veh_compare.vehConf.tooltips
        if self._customCamo:
            title = title.camoInfo
        else:
            title = title.defCamoInfo
        return formatters.packTextBlockData(text=text_styles.standard(backport.text(title())), padding=formatters.packPadding(top=-6, left=-2, bottom=-6))


class VehCmpSkillsTooltip(BlocksTooltipData):

    def __init__(self, context):
        super(VehCmpSkillsTooltip, self).__init__(context, TOOLTIP_TYPE.VEH_CMP_CUSTOMIZATION)
        self._setContentMargin(top=0, left=30, bottom=25, right=30)
        self._setMargins(afterBlock=20, afterSeparator=20)
        self._setWidth(420)

    def _packBlocks(self, *args):
        items = [
         self._packTitleBlock(),
         self.__packDescBlock(),
         self.__packSkillsBlock()]
        return items

    @staticmethod
    def _packTitleBlock():
        return formatters.packImageTextBlockData(title=text_styles.highTitle(VEH_COMPARE.VEHCONF_TOOLTIPS_SKILLS_HEADER), padding={'top': 20})

    @staticmethod
    def __packDescBlock():
        blocks = [
         formatters.packImageTextBlockData(title=text_styles.middleTitle(VEH_COMPARE.VEHCONF_TOOLTIPS_SKILLS_DESCHEADER)),
         formatters.packImageTextBlockData(title=text_styles.main(_ms(VEH_COMPARE.VEHCONF_TOOLTIPS_SKILLS_DESC1, influence=text_styles.alert(VEH_COMPARE.VEHCONF_TOOLTIPS_SKILLS_DESC1_INFLUENCE))), img=RES_ICONS.MAPS_ICONS_LIBRARY_COUNTER_1, imgPadding={'top': 3}, txtOffset=35),
         formatters.packImageTextBlockData(title=text_styles.main(_ms(VEH_COMPARE.VEHCONF_TOOLTIPS_SKILLS_DESC2, perc=text_styles.alert(VEH_COMPARE.VEHCONF_TOOLTIPS_SKILLS_DESC2_PERC))), img=RES_ICONS.MAPS_ICONS_LIBRARY_COUNTER_2, imgPadding={'top': 3}, txtOffset=35)]
        return formatters.packBuildUpBlockData(blocks, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE, gap=15)

    @staticmethod
    def __packSkillsBlock():

        def __packSkill(crewRole, skills):
            skills = cmp_helpers.sortSkills(skills)
            skillsStr = (' ').join(icons.makeImageTag(getSkillSmallIconPath(skillType), 14, 14, 0, 0) for skillType in skills)
            return formatters.packCrewSkillsBlockData(text_styles.main(ITEM_TYPES.tankman_roles(crewRole)), skillsStr, getRoleWhiteIconPath(crewRole), padding={'left': -10})

        blocks = [
         formatters.packImageTextBlockData(title=text_styles.middleTitle(VEH_COMPARE.VEHCONF_TOOLTIPS_SKILLS_SKILLSLIST), padding={'bottom': 10})]
        configurator_view = cmp_helpers.getCmpConfiguratorMainView()
        configured_vehicle = configurator_view.getCurrentVehicle()
        skills_by_roles = cmp_helpers.getVehicleCrewSkills(configured_vehicle)
        skills_by_roles.sort(key=(lambda (role, skillsSet): Tankman.TANKMEN_ROLES_ORDER[role]))
        blocks.extend(__packSkill(*data) for data in skills_by_roles)
        return formatters.packBuildUpBlockData(blocks, gap=0, padding={'bottom': -10})