# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-mac/Carbon/OSAconst.py


def FOUR_CHAR_CODE(x):
    return x


from Carbon.AppleEvents import *
kAEUseStandardDispatch = -1
kOSAComponentType = FOUR_CHAR_CODE('osa ')
kOSAGenericScriptingComponentSubtype = FOUR_CHAR_CODE('scpt')
kOSAFileType = FOUR_CHAR_CODE('osas')
kOSASuite = FOUR_CHAR_CODE('ascr')
kOSARecordedText = FOUR_CHAR_CODE('recd')
kOSAScriptIsModified = FOUR_CHAR_CODE('modi')
kOSAScriptIsTypeCompiledScript = FOUR_CHAR_CODE('cscr')
kOSAScriptIsTypeScriptValue = FOUR_CHAR_CODE('valu')
kOSAScriptIsTypeScriptContext = FOUR_CHAR_CODE('cntx')
kOSAScriptBestType = FOUR_CHAR_CODE('best')
kOSACanGetSource = FOUR_CHAR_CODE('gsrc')
typeOSADialectInfo = FOUR_CHAR_CODE('difo')
keyOSADialectName = FOUR_CHAR_CODE('dnam')
keyOSADialectCode = FOUR_CHAR_CODE('dcod')
keyOSADialectLangCode = FOUR_CHAR_CODE('dlcd')
keyOSADialectScriptCode = FOUR_CHAR_CODE('dscd')
kOSANullScript = 0
kOSANullMode = 0
kOSAModeNull = 0
kOSASupportsCompiling = 2
kOSASupportsGetSource = 4
kOSASupportsAECoercion = 8
kOSASupportsAESending = 16
kOSASupportsRecording = 32
kOSASupportsConvenience = 64
kOSASupportsDialects = 128
kOSASupportsEventHandling = 256
kOSASelectLoad = 1
kOSASelectStore = 2
kOSASelectExecute = 3
kOSASelectDisplay = 4
kOSASelectScriptError = 5
kOSASelectDispose = 6
kOSASelectSetScriptInfo = 7
kOSASelectGetScriptInfo = 8
kOSASelectSetActiveProc = 9
kOSASelectGetActiveProc = 10
kOSASelectScriptingComponentName = 258
kOSASelectCompile = 259
kOSASelectCopyID = 260
kOSASelectCopyScript = 261
kOSASelectGetSource = 513
kOSASelectCoerceFromDesc = 769
kOSASelectCoerceToDesc = 770
kOSASelectSetSendProc = 1025
kOSASelectGetSendProc = 1026
kOSASelectSetCreateProc = 1027
kOSASelectGetCreateProc = 1028
kOSASelectSetDefaultTarget = 1029
kOSASelectStartRecording = 1281
kOSASelectStopRecording = 1282
kOSASelectLoadExecute = 1537
kOSASelectCompileExecute = 1538
kOSASelectDoScript = 1539
kOSASelectSetCurrentDialect = 1793
kOSASelectGetCurrentDialect = 1794
kOSASelectAvailableDialects = 1795
kOSASelectGetDialectInfo = 1796
kOSASelectAvailableDialectCodeList = 1797
kOSASelectSetResumeDispatchProc = 2049
kOSASelectGetResumeDispatchProc = 2050
kOSASelectExecuteEvent = 2051
kOSASelectDoEvent = 2052
kOSASelectMakeContext = 2053
kOSADebuggerCreateSession = 2305
kOSADebuggerGetSessionState = 2306
kOSADebuggerSessionStep = 2307
kOSADebuggerDisposeSession = 2308
kOSADebuggerGetStatementRanges = 2309
kOSADebuggerGetBreakpoint = 2320
kOSADebuggerSetBreakpoint = 2321
kOSADebuggerGetDefaultBreakpoint = 2322
kOSADebuggerGetCurrentCallFrame = 2310
kOSADebuggerGetCallFrameState = 2311
kOSADebuggerGetVariable = 2312
kOSADebuggerSetVariable = 2313
kOSADebuggerGetPreviousCallFrame = 2314
kOSADebuggerDisposeCallFrame = 2315
kOSADebuggerCountVariables = 2316
kOSASelectComponentSpecificStart = 4097
kOSAModePreventGetSource = 1
kOSAModeNeverInteract = kAENeverInteract
kOSAModeCanInteract = kAECanInteract
kOSAModeAlwaysInteract = kAEAlwaysInteract
kOSAModeDontReconnect = kAEDontReconnect
kOSAModeCantSwitchLayer = 64
kOSAModeDoRecord = 4096
kOSAModeCompileIntoContext = 2
kOSAModeAugmentContext = 4
kOSAModeDisplayForHumans = 8
kOSAModeDontStoreParent = 65536
kOSAModeDispatchToDirectObject = 131072
kOSAModeDontGetDataForArguments = 262144
kOSAScriptResourceType = kOSAGenericScriptingComponentSubtype
typeOSAGenericStorage = kOSAScriptResourceType
kOSAErrorNumber = keyErrorNumber
kOSAErrorMessage = keyErrorString
kOSAErrorBriefMessage = FOUR_CHAR_CODE('errb')
kOSAErrorApp = FOUR_CHAR_CODE('erap')
kOSAErrorPartialResult = FOUR_CHAR_CODE('ptlr')
kOSAErrorOffendingObject = FOUR_CHAR_CODE('erob')
kOSAErrorExpectedType = FOUR_CHAR_CODE('errt')
kOSAErrorRange = FOUR_CHAR_CODE('erng')
typeOSAErrorRange = FOUR_CHAR_CODE('erng')
keyOSASourceStart = FOUR_CHAR_CODE('srcs')
keyOSASourceEnd = FOUR_CHAR_CODE('srce')
kOSAUseStandardDispatch = kAEUseStandardDispatch
kOSANoDispatch = kAENoDispatch
kOSADontUsePhac = 1
eNotStarted = 0
eRunnable = 1
eRunning = 2
eStopped = 3
eTerminated = 4
eStepOver = 0
eStepIn = 1
eStepOut = 2
eRun = 3
eLocal = 0
eGlobal = 1
eProperties = 2
keyProgramState = FOUR_CHAR_CODE('dsps')
typeStatementRange = FOUR_CHAR_CODE('srng')
keyProcedureName = FOUR_CHAR_CODE('dfnm')
keyStatementRange = FOUR_CHAR_CODE('dfsr')
keyLocalsNames = FOUR_CHAR_CODE('dfln')
keyGlobalsNames = FOUR_CHAR_CODE('dfgn')
keyParamsNames = FOUR_CHAR_CODE('dfpn')