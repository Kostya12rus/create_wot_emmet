# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/layouts.py
from dossiers2.common.DossierBlockBuilders import *
from account_layout import accountDossierLayout
from vehicle_layout import vehicleDossierLayout
from tankman_layout import tmanDossierLayout
from club_layout import rated7x7DossierLayout, clubDossierLayout
from dossiers2.custom.clan_layout import clanDossierLayout
VERSION_RECORD_FORMAT = 'H'
BLOCK_SIZE_RECORD_FORMAT = 'H'