# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/locale/EPIC_BATTLE.py
from debug_utils import LOG_WARNING

class EPIC_BATTLE(object):
    STATUS_TIMELEFT = '#epic_battle:status/timeLeft'
    EPICBATTLEITEM_SUPPLYPOINTS = '#epic_battle:epicBattleItem/supplyPoints'
    TEAM1NAME = '#epic_battle:team1Name'
    TEAM2NAME = '#epic_battle:team2Name'
    LANE_WEST_NAME = '#epic_battle:lane_west_name'
    LANE_CENTRAL_NAME = '#epic_battle:lane_central_name'
    LANE_EAST_NAME = '#epic_battle:lane_east_name'
    MISSION_TITLE = '#epic_battle:mission/title'
    MISSION_ZONE_CLOSING_ATK = '#epic_battle:mission/zone_closing_atk'
    MISSION_ZONE_CLOSING_DEF = '#epic_battle:mission/zone_closing_def'
    EPICTRAINING_INFO_TEAM1LANELABEL = '#epic_battle:epictraining/info/team1LaneLabel'
    EPICTRAINING_INFO_TEAM2LANELABEL = '#epic_battle:epictraining/info/team2LaneLabel'
    EPICTRAINING_INFO_OTHERLABEL = '#epic_battle:epictraining/info/otherLabel'
    ZONE_TIME_LEFT = '#epic_battle:zone/time_left'
    ZONE_TIME_ADDED = '#epic_battle:zone/time_added'
    ZONE_ENEMY_REINFORCED_TEXT = '#epic_battle:zone/enemy_reinforced_text'
    ZONE_CAPTURED_TEXT = '#epic_battle:zone/captured_text'
    ZONE_CAPTURE_TEXT = '#epic_battle:zone/capture_text'
    ZONE_DEFEND_TEXT = '#epic_battle:zone/defend_text'
    ZONE_DESTROY_TEXT = '#epic_battle:zone/destroy_text'
    ZONE_REINFORCEMENTS_TEXT = '#epic_battle:zone/reinforcements_text'
    ZONE_ARRIVED_TEXT = '#epic_battle:zone/arrived_text'
    ZONE_HEADQUARTERS_TEXT = '#epic_battle:zone/headquarters_text'
    ZONE_ZONE_TEXT = '#epic_battle:zone/zone_text'
    ZONE_REACHED_TEXT = '#epic_battle:zone/reached_text'
    ZONE_DESTROYED_TEXT = '#epic_battle:zone/destroyed_text'
    ZONE_LOST_TEXT = '#epic_battle:zone/lost_text'
    BASE_CONTESTED_ATK = '#epic_battle:base/contested_atk'
    BASE_CONTESTED_DEF = '#epic_battle:base/contested_def'
    HQ_UNDER_ATTACK_ATK = '#epic_battle:hq/under_attack_atk'
    HQ_UNDER_ATTACK_DEF = '#epic_battle:hq/under_attack_def'
    ZONE_REINFORCEMENT_TIMER_ATK = '#epic_battle:zone/reinforcement_timer_atk'
    ZONE_REINFORCEMENT_TIMER_DEF = '#epic_battle:zone/reinforcement_timer_def'
    RESPAWN_TANKS_LEFT = '#epic_battle:respawn/tanks_left'
    RESPAWN_DEPLOY_BUTTON = '#epic_battle:respawn/deploy_button'
    GAME_VICTORY = '#epic_battle:game/victory'
    GAME_DEFEAT = '#epic_battle:game/defeat'
    GAME_ALL_HQS_DESTROYED = '#epic_battle:game/all_hqs_destroyed'
    GAME_TIME_OVER = '#epic_battle:game/time_over'
    GAME_ALL_ENEMIES_DEFEATED = '#epic_battle:game/all_enemies_defeated'
    GAME_ALL_TANKS_DEFEATED = '#epic_battle:game/all_tanks_defeated'
    GAME_DRAW = '#epic_battle:game/draw'
    CHAT_SHORTCUTS_ATTENTION_TO_POSITION = '#epic_battle:chat_shortcuts/attention_to_position'
    CHAT_SHORTCUTS_ATTENTION_TO_OBJECTIVE_ATK = '#epic_battle:chat_shortcuts/attention_to_objective_atk'
    CHAT_SHORTCUTS_ATTENTION_TO_OBJECTIVE_DEF = '#epic_battle:chat_shortcuts/attention_to_objective_def'
    PROGRESS_TIMERS_BASE_CAPTURE = '#epic_battle:progress_timers/base_capture'
    PROGRESS_TIMERS_CAPTURED = '#epic_battle:progress_timers/captured'
    PROGRESS_TIMERS_BLOCKED = '#epic_battle:progress_timers/blocked'
    PROGRESS_TIMERS_RESUPPLY = '#epic_battle:progress_timers/resupply'
    PROGRESS_TIMERS_ACTIVE = '#epic_battle:progress_timers/active'
    PROGRESS_TIMERS_UNAVAILABLE = '#epic_battle:progress_timers/unavailable'
    PROGRESS_TIMERS_FULLY_EQUIPPED = '#epic_battle:progress_timers/fully_equipped'
    DESTROY_TIMERS_AIRSTRIKE_TXT = '#epic_battle:destroy_timers/airstrike_txt'
    RESPAWN_AUTO_TIMER_TXT = '#epic_battle:respawn/auto_timer_txt'
    RANK_RANK1 = '#epic_battle:rank/rank1'
    RANK_RANK2 = '#epic_battle:rank/rank2'
    RANK_RANK3 = '#epic_battle:rank/rank3'
    RANK_RANK4 = '#epic_battle:rank/rank4'
    RANK_RANK5 = '#epic_battle:rank/rank5'
    RANK_RANK6 = '#epic_battle:rank/rank6'
    RANK_NO_NAME = '#epic_battle:rank/no_name'
    RANK_PROMOTION = '#epic_battle:rank/promotion'
    RANK_RECERVEUNLOCKED = '#epic_battle:rank/recerveUnlocked'
    RANK_RESERVEUPGRADED = '#epic_battle:rank/reserveUpgraded'
    MISSION_PRIMARY_TITLE = '#epic_battle:mission/primary/title'
    MISSIONS_PRIMARY_ATK_BASE = '#epic_battle:missions/primary/atk/base'
    MISSIONS_PRIMARY_DEF_BASE = '#epic_battle:missions/primary/def/base'
    MISSIONS_PRIMARY_ATK_HQ = '#epic_battle:missions/primary/atk/hq'
    MISSIONS_PRIMARY_DEF_HQ = '#epic_battle:missions/primary/def/hq'
    MISSIONS_PRIMARY_ATK_HQ_SUB_TITLE = '#epic_battle:missions/primary/atk/hq_sub_title'
    MISSIONS_PRIMARY_DEF_HQ_SUB_TITLE = '#epic_battle:missions/primary/def/hq_sub_title'
    MISSIONS_PRIMARY_ATK_HQ_ADDITIONAL_INFO = '#epic_battle:missions/primary/atk/hq_additional_info'
    MISSIONS_PRIMARY_DEF_HQ_ADDITIONAL_INFO = '#epic_battle:missions/primary/def/hq_additional_info'
    MISSIONS_PRIMARY_ATK_LONGDESCRIPTION = '#epic_battle:missions/primary/atk/longdescription'
    MISSIONS_PRIMARY_DEF_LONGDESCRIPTION = '#epic_battle:missions/primary/def/longdescription'
    MISSIONS_UNLOCKTANKLEVEL = '#epic_battle:missions/unlockTankLevel'
    GLOBAL_MSG_SAVE_TANKS_SHORT = '#epic_battle:global_msg/save_tanks_short'
    GLOBAL_MSG_ATK_TIME_SHORT = '#epic_battle:global_msg/atk/time_short'
    GLOBAL_MSG_DEF_TIME_SHORT = '#epic_battle:global_msg/def/time_short'
    GLOBAL_MSG_LANE_WEST_SHORT = '#epic_battle:global_msg/lane/west_short'
    GLOBAL_MSG_LANE_CENTER_SHORT = '#epic_battle:global_msg/lane/center_short'
    GLOBAL_MSG_LANE_EAST_SHORT = '#epic_battle:global_msg/lane/east_short'
    GLOBAL_MSG_ATK_FOCUS_HQ_SHORT = '#epic_battle:global_msg/atk/focus_hq_short'
    GLOBAL_MSG_DEF_FOCUS_HQ_SHORT = '#epic_battle:global_msg/def/focus_hq_short'
    SPECTATOR_MODE_CAMERA_CONTROLS_TITLE = '#epic_battle:spectator_mode/camera_controls_title'
    SPECTATOR_MODE_CAMERA_WASD = '#epic_battle:spectator_mode/camera_wasd'
    SPECTATOR_MODE_CAMERA_MOUSE_ROTATE = '#epic_battle:spectator_mode/camera_mouse_rotate'
    SPECTATOR_MODE_MSG_TITLE = '#epic_battle:spectator_mode/msg_title'
    SPECTATOR_MODE_MSG_TEXT = '#epic_battle:spectator_mode/msg_text'
    SPECTATOR_MODE_FOLLOW_TITLE = '#epic_battle:spectator_mode/follow_title'
    SPECTATOR_MODE_FOLLOW_TEXT = '#epic_battle:spectator_mode/follow_text'
    SPECTATOR_MODE_UNFOLLOW_TITLE = '#epic_battle:spectator_mode/unfollow_title'
    SPECTATOR_MODE_UNFOLLOW_TEXT = '#epic_battle:spectator_mode/unfollow_text'
    REINFORCEMENT_REINFORCEMENT_IN_TEXT = '#epic_battle:reinforcement/reinforcement_in_text'
    REINFORCEMENT_CAPTURE_NEXT_BASE_TEXT = '#epic_battle:reinforcement/capture_next_base_text'
    REINFORCEMENT_UNAVAILABLE = '#epic_battle:reinforcement/unavailable'
    RECOVERY_PANEL_BASE_TEXT = '#epic_battle:recovery_panel/base_text'
    RECOVERY_PANEL_RECOVERY_REQUESTED = '#epic_battle:recovery_panel/recovery_requested'
    RECOVERY_PANEL_RECOVERY_CANCEL = '#epic_battle:recovery_panel/recovery_cancel'
    RECOVERY_PANEL_RECOVERY_CANCELLED = '#epic_battle:recovery_panel/recovery_cancelled'
    ADVANCE_MESSAGE_TXT = '#epic_battle:advance_message_txt'
    RETREAT_MESSAGE_TXT = '#epic_battle:retreat_message_txt'
    ADVANCE_MISSION_TXT = '#epic_battle:advance_mission_txt'
    RETREAT_MISSION_TXT = '#epic_battle:retreat_mission_txt'
    COMMAND_SHORTCUT_TITLE = '#epic_battle:command_shortcut/title'
    RESPAWN_SHOP_TITLE = '#epic_battle:respawn/shop_title'
    RESPAWN_GOLD_AMMO_NOT_AVAILABLE = '#epic_battle:respawn/gold_ammo_not_available'
    HELP_WINDOW_RESERVES = '#epic_battle:help_window/reserves'
    HELP_WINDOW_RESERVES_DESCRIPTION = '#epic_battle:help_window/reserves/description'
    HELP_WINDOW_COMMUNICATION = '#epic_battle:help_window/communication'
    HELP_WINDOW_COMMUNICATION_DESCRIPTION = '#epic_battle:help_window/communication/description'
    HELP_WINDOW_RECOVERY = '#epic_battle:help_window/recovery'
    HELP_WINDOW_RECOVERY_DESCRIPTION = '#epic_battle:help_window/recovery/description'
    HELP_WINDOW_OVERVIEW_MAP = '#epic_battle:help_window/overview_map'
    HELP_WINDOW_OVERVIEW_MAP_DESCRIPTION = '#epic_battle:help_window/overview_map/description'
    RECOVERY_DISABLED = '#epic_battle:recovery/disabled'
    RECOVERY_BLOCKED = '#epic_battle:recovery/Blocked'
    SUPER_PLATOON_PANEL_TITLE = '#epic_battle:super_platoon_panel/title'
    EPIC_BATTLE_META_VIEW_COMMANDER_LEVEL = '#epic_battle:epic_battle_meta_view/commander_level'
    EPIC_BATTLE_META_VIEW_ABILITIES = '#epic_battle:epic_battle_meta_view/abilities'
    EPIC_BATTLE_META_VIEW_MAX_SKILL = '#epic_battle:epic_battle_meta_view/Max_skill'
    EPIC_BATTLE_META_VIEW_ACQUIRE_SKILL = '#epic_battle:epic_battle_meta_view/Acquire_skill'
    OVERTIME_LABEL = '#epic_battle:overtime/label'
    EPICBATTLESCAROUSEL_LOCKEDTOOLTIP_HEADER = '#epic_battle:epicBattlesCarousel/lockedTooltip/header'
    EPICBATTLESCAROUSEL_LOCKEDTOOLTIP_BODY = '#epic_battle:epicBattlesCarousel/lockedTooltip/body'
    EPICBATTLESCAROUSEL_LOBBY_LEVELINFO = '#epic_battle:epicBattlesCarousel/lobby/levelInfo'
    EPICBATTLESCAROUSEL_LOBBY_LEVELINFO_LEVEL = '#epic_battle:epicBattlesCarousel/lobby/levelInfo/level'
    TAB_SCREEN_SHOW_MY_LANE = '#epic_battle:tab_screen/show_my_lane'
    TAB_SCREEN_SHOW_ALL_LANES = '#epic_battle:tab_screen/show_all_lanes'
    IN_GAME_RANK_EXPERIENCE_TEXT = '#epic_battle:in_game_rank/experience_text'
    ZONE_LEAVE_ZONE = '#epic_battle:zone/leave_zone'
    METAABILITYSCREEN_ACTIVATION_DEPENDS = '#epic_battle:metaAbilityScreen/activation_depends'
    METAABILITYSCREEN_ABILITY_NOT_UNLOCKED = '#epic_battle:metaAbilityScreen/Ability_not_unlocked'
    METAABILITYSCREEN_ABILITY_LEVEL = '#epic_battle:metaAbilityScreen/Ability_level'
    METAABILITYSCREEN_HOW_TO_ACTIVATE = '#epic_battle:metaAbilityScreen/how_to_activate'
    SMOKE_IN_SMOKE = '#epic_battle:smoke/In_smoke'
    SMOKE_INALLYSMOKE = '#epic_battle:smoke/InAllySmoke'
    SMOKE_INENEMYSMOKE = '#epic_battle:smoke/InEnemySmoke'
    ABILITYINFO_PARAMS_COMMON_COOLDOWNTIME = '#epic_battle:abilityInfo/params/common/cooldownTime'
    ABILITYINFO_PARAMS_COMMON_DELAY = '#epic_battle:abilityInfo/params/common/delay'
    ABILITYINFO_PARAMS_ARTILLERY_AREARADIUS = '#epic_battle:abilityInfo/params/artillery/areaRadius'
    ABILITYINFO_PARAMS_ARTILLERY_SHOTSNUMBER = '#epic_battle:abilityInfo/params/artillery/shotsNumber'
    ABILITYINFO_PARAMS_ARTILLERY_DURATION = '#epic_battle:abilityInfo/params/artillery/duration'
    ABILITYINFO_PARAMS_AIRSTRIKE_DROPAREA = '#epic_battle:abilityInfo/params/airstrike/dropArea'
    ABILITYINFO_PARAMS_AIRSTRIKE_BOMBSNUMBER = '#epic_battle:abilityInfo/params/airstrike/bombsNumber'
    ABILITYINFO_PARAMS_AIRSTRIKE_STUN = '#epic_battle:abilityInfo/params/airstrike/stun'
    ABILITYINFO_PARAMS_RECON_REVEALEDAREA = '#epic_battle:abilityInfo/params/recon/revealedArea'
    ABILITYINFO_PARAMS_RECON_REVEALEDAREA_VALUE = '#epic_battle:abilityInfo/params/recon/revealedArea/value'
    ABILITYINFO_PARAMS_RECON_SPOTTINGDURATION = '#epic_battle:abilityInfo/params/recon/spottingDuration'
    ABILITYINFO_PARAMS_RECON_DELAY = '#epic_battle:abilityInfo/params/recon/delay'
    ABILITYINFO_PARAMS_INSPIRE_RADIUS = '#epic_battle:abilityInfo/params/inspire/radius'
    ABILITYINFO_PARAMS_INSPIRE_DURATION = '#epic_battle:abilityInfo/params/inspire/duration'
    ABILITYINFO_PARAMS_INSPIRE_INACTIVATIONDELAY = '#epic_battle:abilityInfo/params/inspire/inactivationDelay'
    ABILITYINFO_PARAMS_INSPIRE_CREWROLESFACTOR = '#epic_battle:abilityInfo/params/inspire/crewRolesFactor'
    ABILITYINFO_PARAMS_INSPIRE_SELFINCREASEFACTORS = '#epic_battle:abilityInfo/params/inspire/selfIncreaseFactors'
    ABILITYINFO_PARAMS_SMOKE_TARGETEDAREA = '#epic_battle:abilityInfo/params/smoke/targetedArea'
    ABILITYINFO_PARAMS_SMOKE_PROJECTILESNUMBER = '#epic_battle:abilityInfo/params/smoke/projectilesNumber'
    ABILITYINFO_PARAMS_SMOKE_TOTALDURATION = '#epic_battle:abilityInfo/params/smoke/totalDuration'
    ABILITYINFO_PARAMS_SMOKE_VISIONRADIUSFACTOR = '#epic_battle:abilityInfo/params/smoke/visionRadiusFactor'
    ABILITYINFO_PARAMS_PASSIVE_ENGINEERING_RESUPPLYCOOLDOWNFACTOR = '#epic_battle:abilityInfo/params/passive_engineering/resupplyCooldownFactor'
    ABILITYINFO_PARAMS_PASSIVE_ENGINEERING_RESUPPLYSHELLSFACTOR = '#epic_battle:abilityInfo/params/passive_engineering/resupplyShellsFactor'
    ABILITYINFO_PARAMS_PASSIVE_ENGINEERING_CAPTURESPEEDFACTOR = '#epic_battle:abilityInfo/params/passive_engineering/captureSpeedFactor'
    ABILITYINFO_PARAMS_PASSIVE_ENGINEERING_CAPTUREBLOCKBONUSTIME = '#epic_battle:abilityInfo/params/passive_engineering/captureBlockBonusTime'
    ABILITYINFO_PARAMS_STEALTH_RADAR_PASSIVECIRCULARVISIONRADIUS = '#epic_battle:abilityInfo/params/stealth_radar/passiveCircularVisionRadius'
    ABILITYINFO_PARAMS_STEALTH_RADAR_DURATION = '#epic_battle:abilityInfo/params/stealth_radar/duration'
    ABILITYINFO_PARAMS_STEALTH_RADAR_DEMASKFOLIAGEFACTOR = '#epic_battle:abilityInfo/params/stealth_radar/demaskFoliageFactor'
    ABILITYINFO_PARAMS_STEALTH_RADAR_DEMASKMOVINGFACTOR = '#epic_battle:abilityInfo/params/stealth_radar/demaskMovingFactor'
    ABILITYINFO_PARAMS_STEALTH_RADAR_INVISIBILITYADDITIVETERM = '#epic_battle:abilityInfo/params/stealth_radar/invisibilityAdditiveTerm'
    ABILITYINFO_PARAMS_FL_REGENERATIONKIT_HEALTIME = '#epic_battle:abilityInfo/params/fl_regenerationKit/healTime'
    ABILITYINFO_PARAMS_FL_REGENERATIONKIT_HEALTHREGENPERTICK = '#epic_battle:abilityInfo/params/fl_regenerationKit/healthRegenPerTick'
    ABILITYINFO_PARAMS_FL_REGENERATIONKIT_INITIALHEAL = '#epic_battle:abilityInfo/params/fl_regenerationKit/initialHeal'
    ABILITYINFO_PARAMS_FL_REGENERATIONKIT_RESUPPLYHEALTHPOINTSFACTOR = '#epic_battle:abilityInfo/params/fl_regenerationKit/resupplyHealthPointsFactor'
    ABILITYINFO_PARAMS_FL_REGENERATIONKIT_MINESDAMAGEREDUCEFACTOR = '#epic_battle:abilityInfo/params/fl_regenerationKit/minesDamageReduceFactor'
    ABILITYINFO_PARAMS_FL_REGENERATIONKIT_MINESDAMAGEREDUCEFACTOR_VALUE = '#epic_battle:abilityInfo/params/fl_regenerationKit/minesDamageReduceFactor/value'
    ABILITYINFO_PARAMS_ARCADE_MINEFIELD_EPIC_BATTLE_LIFETIME = '#epic_battle:abilityInfo/params/arcade_minefield_epic_battle/lifetime'
    ABILITYINFO_PARAMS_ARCADE_MINEFIELD_EPIC_BATTLE_SHELL = '#epic_battle:abilityInfo/params/arcade_minefield_epic_battle/shell'
    ABILITYINFO_PARAMS_ARCADE_MINEFIELD_EPIC_BATTLE_BOMBSNUMBER = '#epic_battle:abilityInfo/params/arcade_minefield_epic_battle/bombsNumber'
    EQUIPMENT_HEALPOINT_HEALING = '#epic_battle:equipment/healPoint/healing'
    EQUIPMENT_HEALPOINT_HEALED = '#epic_battle:equipment/healPoint/healed'
    ABILITYINFO_UNITS_METER = '#epic_battle:abilityInfo/units/meter'
    ABILITYINFO_UNITS_SECONDS = '#epic_battle:abilityInfo/units/seconds'
    ABILITYINFO_PROPERTIES_STATIC = '#epic_battle:abilityInfo/properties/static'
    ABILITYINFO_PROPERTIES_DYNAMIC = '#epic_battle:abilityInfo/properties/dynamic'
    ABILITYINFO_MANAGE_ABILITIES = '#epic_battle:abilityInfo/manage_abilities'
    ABILITYINFO_MANAGE_ABILITIES_DESC = '#epic_battle:abilityInfo/manage_abilities_desc'
    INSPIRE_INSPIRING = '#epic_battle:inspire/inspiring'
    INSPIRE_INSPIRED = '#epic_battle:inspire/inspired'
    SCOREPANEL_STAGE1 = '#epic_battle:scorePanel/stage1'
    SCOREPANEL_STAGE2 = '#epic_battle:scorePanel/stage2'
    SCOREPANEL_STAGE3 = '#epic_battle:scorePanel/stage3'
    STEALTHRADAR_ACTIVE = '#epic_battle:stealthRadar/active'
    STEALTHRADAR_INACTIVE = '#epic_battle:stealthRadar/inactive'
    REINFORCEMENTSPANEL_INTEXT = '#epic_battle:reinforcementsPanel/inText'
    RESPAWNSCREEN_DEPLOYMENTLANE1 = '#epic_battle:respawnScreen/deploymentLane1'
    RESPAWNSCREEN_DEPLOYMENTLANE2 = '#epic_battle:respawnScreen/deploymentLane2'
    RESPAWNSCREEN_DEPLOYMENTLANE3 = '#epic_battle:respawnScreen/deploymentLane3'
    RESPAWNSCREEN_SECONDSTIMERTEXT = '#epic_battle:respawnScreen/secondsTimerText'
    RESPAWNSCREEN_HEADERTITLE = '#epic_battle:respawnScreen/headerTitle'
    RESPAWNSCREEN_RESPAWNWARNING = '#epic_battle:respawnScreen/respawnWarning'
    PLAYER_ERRORS_MINEFIELDISINTERSECTED = '#epic_battle:player_errors/minefieldIsIntersected'
    DEPLOYMENTMAP_SPGLIMITREACHED = '#epic_battle:deploymentMap/spgLimitReached'
    DEPLOYMENTMAP_LANEPLAYERLIMITREACHED = '#epic_battle:deploymentMap/lanePlayerLimitReached'
    DEPLOYMENTMAP_RESPAWNWARNING = '#epic_battle:deploymentMap/respawnWarning'
    EPIC_BATTLES_AFTER_BATTLE_TITLE = '#epic_battle:epic_battles_after_battle/Title'
    EPIC_BATTLES_AFTER_BATTLE_ACHIEVED_RANK = '#epic_battle:epic_battles_after_battle/Achieved_Rank'
    EPIC_BATTLES_AFTER_BATTLE_LEVEL_UP_TITLE = '#epic_battle:epic_battles_after_battle/Level_Up_Title'
    EPIC_BATTLES_AFTER_BATTLE_MAX_LEVEL_INFO_TITLE = '#epic_battle:epic_battles_after_battle/max_level_info/title'
    EPIC_BATTLES_AFTER_BATTLE_MAX_LEVEL_INFO_DESCRIPTION = '#epic_battle:epic_battles_after_battle/max_level_info/description'
    SELECTORTOOLTIP_EPICBATTLE_HEADER = '#epic_battle:selectorTooltip/epicBattle/header'
    SELECTORTOOLTIP_EPICBATTLE_BODY = '#epic_battle:selectorTooltip/epicBattle/body'
    SELECTORTOOLTIP_EPICBATTLE_BODYVEHICLELEVEL = '#epic_battle:selectorTooltip/epicBattle/bodyVehicleLevel'
    SELECTORTOOLTIP_EPICBATTLE_FROZEN = '#epic_battle:selectorTooltip/epicBattle/frozen'
    SELECTORTOOLTIP_EPICBATTLE_TIMETABLE_TITLE = '#epic_battle:selectorTooltip/epicBattle/timeTable/title'
    SELECTORTOOLTIP_EPICBATTLE_TIMETABLE_TODAY = '#epic_battle:selectorTooltip/epicBattle/timeTable/today'
    SELECTORTOOLTIP_EPICBATTLE_TIMETABLE_TOMORROW = '#epic_battle:selectorTooltip/epicBattle/timeTable/tomorrow'
    SELECTORTOOLTIP_EPICBATTLE_TIMETABLE_DASH = '#epic_battle:selectorTooltip/epicBattle/timeTable/dash'
    SELECTORTOOLTIP_EPICBATTLE_TIMELEFT = '#epic_battle:selectorTooltip/epicBattle/timeLeft'
    SELECTORTOOLTIP_EPICBATTLE_STARTIN = '#epic_battle:selectorTooltip/epicBattle/startIn'
    SELECTORTOOLTIP_EPICBATTLE_ATTENTION_ASSUREDLOWPERFORMANCE_TITLE = '#epic_battle:selectorTooltip/epicBattle/attention/assuredLowPerformance/title'
    SELECTORTOOLTIP_EPICBATTLE_ATTENTION_ASSUREDLOWPERFORMANCE_DESCRIPTION = '#epic_battle:selectorTooltip/epicBattle/attention/assuredLowPerformance/description'
    SELECTORTOOLTIP_EPICBATTLE_ATTENTION_POSSIBLELOWPERFORMANCE_TITLE = '#epic_battle:selectorTooltip/epicBattle/attention/possibleLowPerformance/title'
    SELECTORTOOLTIP_EPICBATTLE_ATTENTION_POSSIBLELOWPERFORMANCE_DESCRIPTION = '#epic_battle:selectorTooltip/epicBattle/attention/possibleLowPerformance/description'
    SELECTORTOOLTIP_EPICBATTLE_ATTENTION_INFORMATIVELOWPERFORMANCE_TITLE = '#epic_battle:selectorTooltip/epicBattle/attention/informativeLowPerformance/title'
    SELECTORTOOLTIP_EPICBATTLE_ATTENTION_INFORMATIVELOWPERFORMANCE_DESCRIPTION = '#epic_battle:selectorTooltip/epicBattle/attention/informativeLowPerformance/description'
    QUESTSTOOLTIP_EPICBATTLE_HEADER = '#epic_battle:questsTooltip/epicBattle/header'
    QUESTSTOOLTIP_EPICBATTLE_STEELHUNTER_HEADER = '#epic_battle:questsTooltip/epicBattle/steelhunter/header'
    QUESTSTOOLTIP_EPICBATTLE_TIMELEFT = '#epic_battle:questsTooltip/epicBattle/timeLeft'
    QUESTSTOOLTIP_EPICBATTLE_STARTIN = '#epic_battle:questsTooltip/epicBattle/startIn'
    QUESTSTOOLTIP_EPICBATTLE_LESSTHANDAY = '#epic_battle:questsTooltip/epicBattle/lessThanDay'
    QUESTSTOOLTIP_EPICBATTLE_UNAVAILABLE = '#epic_battle:questsTooltip/epicBattle/unavailable'
    QUESTSTOOLTIP_EPICBATTLE_RESTRICT_LEVEL = '#epic_battle:questsTooltip/epicBattle/restrict/level'
    WIDGETALERTMESSAGEBLOCK_NOCYCLEMESSAGE = '#epic_battle:widgetAlertMessageBlock/noCycleMessage'
    WIDGETALERTMESSAGEBLOCK_ALLPERIPHERIESHALT = '#epic_battle:widgetAlertMessageBlock/allPeripheriesHalt'
    WIDGETALERTMESSAGEBLOCK_SOMEPERIPHERIESHALT = '#epic_battle:widgetAlertMessageBlock/somePeripheriesHalt'
    WIDGETALERTMESSAGEBLOCK_SINGLEMODEHALT = '#epic_battle:widgetAlertMessageBlock/singleModeHalt'
    WIDGETALERTMESSAGEBLOCK_BUTTON = '#epic_battle:widgetAlertMessageBlock/button'
    WIDGETALERTMESSAGEBLOCK_STARTIN = '#epic_battle:widgetAlertMessageBlock/startIn'
    WIDGETALERTMESSAGEBLOCK_ANNOUNCEMENT = '#epic_battle:widgetAlertMessageBlock/announcement'
    STATUS_TIMELEFT_DAYS = '#epic_battle:status/timeLeft/days'
    STATUS_TIMELEFT_HOURS = '#epic_battle:status/timeLeft/hours'
    STATUS_TIMELEFT_MIN = '#epic_battle:status/timeLeft/min'
    STATUS_TIMELEFT_LESSMIN = '#epic_battle:status/timeLeft/lessMin'
    BATTLERESULTS_SPOTTING = '#epic_battle:battleResults/spotting'
    BATTLERESULTS_ASSISTANCE = '#epic_battle:battleResults/assistance'
    BATTLERESULTS_ARMOR = '#epic_battle:battleResults/armor'
    BATTLERESULTS_CRITS = '#epic_battle:battleResults/crits'
    BATTLERESULTS_KILL = '#epic_battle:battleResults/kill'
    BATTLERESULTS_DAMAGE = '#epic_battle:battleResults/damage'
    METAABILITYSCREEN_ABILITY_MAX_LEVEL = '#epic_battle:metaAbilityScreen/Ability_max_level'
    METAABILITYSCREEN_ABILITY_LOCKED = '#epic_battle:metaAbilityScreen/Ability_locked'
    METAABILITYSCREEN_ABILITY_NOT_POINTS = '#epic_battle:metaAbilityScreen/Ability_not_points'
    BOOSTER_DESCRIPTION_BONUSVALUETIME_BOOSTER_XP = '#epic_battle:booster/description/bonusValueTime/booster_xp'
    BOOSTER_DESCRIPTION_BONUSVALUETIME_BOOSTER_FREE_XP = '#epic_battle:booster/description/bonusValueTime/booster_free_xp'
    BOOSTER_DESCRIPTION_BONUSVALUETIME_BOOSTER_CREW_XP = '#epic_battle:booster/description/bonusValueTime/booster_crew_xp'
    PRIMETIME_TITLE = '#epic_battle:primeTime/title'
    PRIMETIME_STEELHUNTER_TITLE = '#epic_battle:primeTime/steelhunter/title'
    PRIMETIME_TITLEWELCOME = '#epic_battle:primeTime/titleWelcome'
    PRIMETIME_APPLYBTN = '#epic_battle:primeTime/applyBtn'
    PRIMETIME_CANCELBTN = '#epic_battle:primeTime/cancelBtn'
    PRIMETIME_CONTINUEBTN = '#epic_battle:primeTime/continueBtn'
    PRIMETIME_SERVERTOOLTIP = '#epic_battle:primeTime/serverTooltip'
    PRIMETIME_SERVERUNAVAILABLETOOLTIP = '#epic_battle:primeTime/serverUnavailableTooltip'
    PRIMETIME_SERVERS = '#epic_battle:primeTime/servers'
    PRIMETIME_STATUS_NOPRIMETIMEONTHISSERVER = '#epic_battle:primeTime/status/noPrimeTimeOnThisServer'
    PRIMETIME_STATUS_CYCLEFINISHEDONTHISSERVER = '#epic_battle:primeTime/status/cycleFinishedOnThisServer'
    PRIMETIME_STATUS_NOPRIMETIMESONALLSERVERS = '#epic_battle:primeTime/status/noPrimeTimesOnAllServers'
    PRIMETIME_STATUS_DISABLEDONTHISSERVER = '#epic_battle:primeTime/status/disabledOnThisServer'
    PRIMETIME_MANYSERVERSAVAILABLE = '#epic_battle:primeTime/manyServersAvailable'
    PRIMETIME_ONESERVERAVAILABLE = '#epic_battle:primeTime/oneServerAvailable'
    PRIMETIME_PRIMEISAVAILABLE = '#epic_battle:primeTime/primeIsAvailable'
    PRIMETIME_PRIMEWILLBEAVAILABLE = '#epic_battle:primeTime/primeWillBeAvailable'
    PRIMETIME_ENDOFCYCLE = '#epic_battle:primeTime/endOfCycle'
    PRIMETIME_STATUS_THISENABLE = '#epic_battle:primeTime/status/thisEnable'
    PRIMETIME_STATUS_DISABLE = '#epic_battle:primeTime/status/disable'
    TUTORIAL_HINT_EPICRESERVESSLOTHINT = '#epic_battle:tutorial/hint/epicReservesSlotHint'
    SEASON_201902_NAME = '#epic_battle:season/201902/name'
    SEASON_202002_NAME = '#epic_battle:season/202002/name'
    SEASON_202108_NAME = '#epic_battle:season/202108/name'
    EPICBATTLEITEM_SUPPLYPOINTS_HEADER = '#epic_battle:epicBattleItem/supplyPoints/header'
    EPICBATTLEITEM_SUPPLYPOINTS_DESCRIPTION = '#epic_battle:epicBattleItem/supplyPoints/description'
    EPICBATTLEITEM_SUPPLYPOINTS_BODY = '#epic_battle:epicBattleItem/supplyPoints/body'
    INTRO_TITLE = '#epic_battle:intro/title'
    INTRO_CONFIRM = '#epic_battle:intro/confirm'
    INTRO_CARD_CATEGORIES_TITLE = '#epic_battle:intro/card/categories/title'
    INTRO_CARD_CATEGORIES_DESC = '#epic_battle:intro/card/categories/desc'
    INTRO_CARD_SLOTS_TITLE = '#epic_battle:intro/card/slots/title'
    INTRO_CARD_SLOTS_DESC = '#epic_battle:intro/card/slots/desc'
    INTRO_CARD_TYPES_TITLE = '#epic_battle:intro/card/types/title'
    INTRO_CARD_TYPES_DESC = '#epic_battle:intro/card/types/desc'
    TOOLTIPS_TIMETOSTART_SEASON = '#epic_battle:tooltips/timeToStart/season'
    TOOLTIPS_TIMETOEND_SEASON = '#epic_battle:tooltips/timeToEnd/season'
    TOOLTIPS_TIMETOSTART_CYCLE = '#epic_battle:tooltips/timeToStart/cycle'
    TOOLTIPS_TIMETOEND_CYCLE = '#epic_battle:tooltips/timeToEnd/cycle'
    TOOLTIPS_COMMON_DISABLED = '#epic_battle:tooltips/common/disabled'
    TOOLTIPS_COMMON_TITLE = '#epic_battle:tooltips/common/title'
    TOOLTIPS_COMMON_TITLEWITHCYCLE = '#epic_battle:tooltips/common/titleWithCycle'
    TOOLTIPS_WIDGET_REACHEDMAXLEVEL = '#epic_battle:tooltips/widget/reachedMaxLevel'
    TOOLTIPS_WIDGET_LEVEL = '#epic_battle:tooltips/widget/level'
    TOOLTIPS_WIDGET_ALLCYCLESFINISHED = '#epic_battle:tooltips/widget/allCyclesFinished'
    TOOLTIPS_WIDGET_SEASONFINISHED = '#epic_battle:tooltips/widget/seasonFinished'
    TOOLTIPS_SLOTUNLOCKED_MESSAGE = '#epic_battle:tooltips/slotUnlocked/message'
    TOOLTIPS_SLOTSETUPINFO_TITLE_LIGHTTANK = '#epic_battle:tooltips/slotSetupInfo/title/lightTank'
    TOOLTIPS_SLOTSETUPINFO_TITLE_MEDIUMTANK = '#epic_battle:tooltips/slotSetupInfo/title/mediumTank'
    TOOLTIPS_SLOTSETUPINFO_TITLE_HEAVYTANK = '#epic_battle:tooltips/slotSetupInfo/title/heavyTank'
    TOOLTIPS_SLOTSETUPINFO_TITLE_SPG = '#epic_battle:tooltips/slotSetupInfo/title/SPG'
    TOOLTIPS_SLOTSETUPINFO_TITLE_AT_SPG = '#epic_battle:tooltips/slotSetupInfo/title/AT-SPG'
    TOOLTIPS_SLOTSETUPINFO_SUBTITLE = '#epic_battle:tooltips/slotSetupInfo/subtitle'
    TOOLTIPS_SLOTSETUPINFO_SCHEME = '#epic_battle:tooltips/slotSetupInfo/scheme'
    TOOLTIPS_SLOTSETUPINFO_OPEN_TITLE = '#epic_battle:tooltips/slotSetupInfo/open/title'
    TOOLTIPS_SLOTSETUPINFO_OPEN_DESC = '#epic_battle:tooltips/slotSetupInfo/open/desc'
    TOOLTIPS_SLOTSETUPINFO_UPGRADE_TITLE = '#epic_battle:tooltips/slotSetupInfo/upgrade/title'
    TOOLTIPS_SLOTSETUPINFO_UPGRADE_DESC = '#epic_battle:tooltips/slotSetupInfo/upgrade/desc'
    RANK_RANK_ENUM = (
     RANK_RANK1,
     RANK_RANK2,
     RANK_RANK3,
     RANK_RANK4,
     RANK_RANK5,
     RANK_RANK6)
    SEASON_ALL_NAME_ENUM = (
     SEASON_201902_NAME,
     SEASON_202002_NAME,
     SEASON_202108_NAME)

    @classmethod
    def getRankLabel(cls, key0):
        outcome = ('#epic_battle:rank/rank{}').format(key0)
        if outcome not in cls.RANK_RANK_ENUM:
            LOG_WARNING(('Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getSeasonName(cls, key0):
        outcome = ('#epic_battle:season/{}/name').format(key0)
        if outcome not in cls.SEASON_ALL_NAME_ENUM:
            LOG_WARNING(('Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome