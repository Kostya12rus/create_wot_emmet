# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/__init__.py
import enumerations
BTMS_COMMANDS = enumerations.Enumeration('Battle messenger commands', [
 (
  'ChannelsInit', (lambda : 'Messenger.Battle.ChannelsInit')),
 (
  'CheckCooldownPeriod', (lambda : 'Messenger.Battle.CheckCooldownPeriod')),
 (
  'SendMessage', (lambda : 'Messenger.Battle.SendMessage')),
 (
  'ReceiveMessage', (lambda : 'Messenger.Battle.RecieveMessage')),
 (
  'ClearMessages', (lambda : 'Messenger.Battle.ClearMessages')),
 (
  'PopulateUI', (lambda : 'Messenger.Battle.PopulateUI')),
 (
  'RefreshUI', (lambda : 'Messenger.Battle.RefreshUI')),
 (
  'ChangeFocus', (lambda : 'Messenger.Battle.ChangeFocus')),
 (
  'JoinToChannel', (lambda : 'Messenger.Battle.JoinToChannel')),
 (
  'ShowActionFailureMessage', (lambda : 'Messenger.Battle.ShowActionFailureMesssage')),
 (
  'UpdateReceivers', (lambda : 'Messenger.Battle.UpdateReceivers')),
 (
  'UserPreferencesUpdated', (lambda : 'Messenger.Battle.UserPreferencesUpdated')),
 (
  'ReceiverChanged', (lambda : 'Messenger.Battle.ReceiverChanged')),
 (
  'AddToFriends', (lambda : 'Battle.UsersRoster.AddToFriends')),
 (
  'RemoveFromFriends', (lambda : 'Battle.UsersRoster.RemoveFromFriends')),
 (
  'AddToIgnored', (lambda : 'Battle.UsersRoster.AddToIgnored')),
 (
  'RemoveFromIgnored', (lambda : 'Battle.UsersRoster.RemoveFromIgnored')),
 (
  'AddMuted', (lambda : 'Battle.UsersRoster.AddMuted')),
 (
  'RemoveMuted', (lambda : 'Battle.UsersRoster.RemoveMuted')),
 (
  'isHistoryEnabled', (lambda : 'Messenger.Battle.isHistoryEnabled')),
 (
  'upHistory', (lambda : 'Messenger.Battle.upHistory')),
 (
  'downHistory', (lambda : 'Messenger.Battle.downHistory')),
 (
  'EnabledHistoryControls', (lambda : 'Messenger.Battle.EnabledHistoryControls')),
 (
  'GetLatestHistory', (lambda : 'Messenger.Battle.GetLatestHistory')),
 (
  'ShowHistoryMessages', (lambda : 'Messenger.Battle.ShowHistoryMessages')),
 (
  'GetLastMessages', (lambda : 'Messenger.Battle.GetLastMessages')),
 (
  'ShowLatestMessages', (lambda : 'Messenger.Battle.ShowLatestMessages'))], instance=enumerations.CallabbleEnumItem)

class FILL_COLORS(object):
    BLACK = 'black'
    BROWN = 'brown'
    GREEN = 'green'
    RED = 'red'