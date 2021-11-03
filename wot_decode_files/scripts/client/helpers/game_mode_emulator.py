# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/game_mode_emulator.py
import sys
DEFAULT_VISIBILITY_MASK = -1
GAME_MODE_VISIBILITY_MASKS = {'capture_the_flag': 1, 
   'domination': 2, 
   'assault': 4, 
   'nations': 8, 
   'capture_the_flag_2': 16, 
   'domination_2': 32, 
   'assault_2': 64, 
   'fallout_bomb': 128, 
   'fallout_2_flag': 256, 
   'fallout_3': 512, 
   'fallout_4': 1024, 
   'capture_the_flag_30_vs_30': 2048, 
   'domination_30_vs_30': 4096, 
   'sandbox': 8192, 
   'bootcamp': 16384, 
   'visible_for_observer': 2147483648}

def gameModeVisibilityMask():
    if 'gameMode' not in sys.argv:
        return DEFAULT_VISIBILITY_MASK
    gameModeArgIndex = sys.argv.index('gameMode') + 1
    if gameModeArgIndex >= len(sys.argv):
        return DEFAULT_VISIBILITY_MASK
    gameMode = sys.argv[gameModeArgIndex].lower()
    if gameMode not in GAME_MODE_VISIBILITY_MASKS:
        return DEFAULT_VISIBILITY_MASK
    return GAME_MODE_VISIBILITY_MASKS[gameMode]