# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/VOIP/VOIPCommon.py
CODE_SUCCESS = 0
CODE_ERROR = 1
STATUS_OK = 0
STATUS_FAILED_TO_CONNECT = 10
STATUS_WRONG_CREDENTIALS = 20
STATUS_UNKNOWN_ACCOUNT = 21
STATUS_UNKNOWN = 1000
STATE_LOGGED_OUT = 0
STATE_LOGGED_IN = 1
STATE_LOGGIN_IN = 2
STATE_LOGGIN_OUT = 3
KEY_RETURN_CODE = 'return_code'
KEY_STATUS_CODE = 'status_code'
KEY_STATUS_STRING = 'status_string'
KEY_COMMAND = 'command'
KEY_STATE = 'state'
KEY_COUNT = 'count'
KEY_CURRENT_CAPTURE_DEVICE = 'current_capture_device'
KEY_CAPTURE_DEVICES = 'capture_devices'
KEY_URI = 'uri'
KEY_IS_SPEAKING = 'is_speaking'
KEY_PARTICIPANT_URI = 'participant_uri'
KEY_PARTICIPANT_PROPERTY_FREQUENCY = 'participant_property_frequency'
KEY_MAX_PORT = 'maximum_port'
KEY_MIN_PORT = 'minimum_port'
KEY_LOG_PREFIX = 'log_prefix'
KEY_LOG_SUFFIX = 'log_suffix'
KEY_LOG_FOLDER = 'log_folder'
KEY_LOG_LEVEL = 'log_level'
KEY_SERVER = 'voip_server'
KEY_VOIP_MASTER = 'masterVivox'
KEY_VOIP_MIC = 'micVivox'
CMD_SET_PARTICIPANT_MUTE = 'set_participant_mute'