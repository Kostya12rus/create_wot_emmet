# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-freebsd6/IN.py
__GNUCLIKE_ASM = 3
__GNUCLIKE_ASM = 2
__GNUCLIKE___TYPEOF = 1
__GNUCLIKE___OFFSETOF = 1
__GNUCLIKE___SECTION = 1
__GNUCLIKE_ATTRIBUTE_MODE_DI = 1
__GNUCLIKE_CTOR_SECTION_HANDLING = 1
__GNUCLIKE_BUILTIN_CONSTANT_P = 1
__GNUCLIKE_BUILTIN_VARARGS = 1
__GNUCLIKE_BUILTIN_STDARG = 1
__GNUCLIKE_BUILTIN_VAALIST = 1
__GNUC_VA_LIST_COMPATIBILITY = 1
__GNUCLIKE_BUILTIN_NEXT_ARG = 1
__GNUCLIKE_BUILTIN_MEMCPY = 1
__CC_SUPPORTS_INLINE = 1
__CC_SUPPORTS___INLINE = 1
__CC_SUPPORTS___INLINE__ = 1
__CC_SUPPORTS___FUNC__ = 1
__CC_SUPPORTS_WARNING = 1
__CC_SUPPORTS_VARADIC_XXX = 1
__CC_SUPPORTS_DYNAMIC_ARRAY_INIT = 1
__CC_INT_IS_32BIT = 1

def __P(protos):
    return protos


def __STRING(x):
    pass


def __XSTRING(x):
    return __STRING(x)


def __P(protos):
    return ()


def __STRING(x):
    return 'x'


def __aligned(x):
    return __attribute__(__aligned__(x))


def __section(x):
    return __attribute__(__section__(x))


def __aligned(x):
    return __attribute__(__aligned__(x))


def __section(x):
    return __attribute__(__section__(x))


def __nonnull(x):
    return __attribute__(__nonnull__(x))


def __predict_true(exp):
    return __builtin_expect(exp, 1)


def __predict_false(exp):
    return __builtin_expect(exp, 0)


def __predict_true(exp):
    return exp


def __predict_false(exp):
    return exp


def __format_arg(fmtarg):
    return __attribute__(__format_arg__(fmtarg))


def __FBSDID(s):
    return __IDSTRING(__CONCAT(__rcsid_, __LINE__), s)


def __RCSID(s):
    return __IDSTRING(__CONCAT(__rcsid_, __LINE__), s)


def __RCSID_SOURCE(s):
    return __IDSTRING(__CONCAT(__rcsid_source_, __LINE__), s)


def __SCCSID(s):
    return __IDSTRING(__CONCAT(__sccsid_, __LINE__), s)


def __COPYRIGHT(s):
    return __IDSTRING(__CONCAT(__copyright_, __LINE__), s)


_POSIX_C_SOURCE = 199009
_POSIX_C_SOURCE = 199209
__XSI_VISIBLE = 600
_POSIX_C_SOURCE = 200112
__XSI_VISIBLE = 500
_POSIX_C_SOURCE = 199506
_POSIX_C_SOURCE = 198808
__POSIX_VISIBLE = 200112
__ISO_C_VISIBLE = 1999
__POSIX_VISIBLE = 199506
__ISO_C_VISIBLE = 1990
__POSIX_VISIBLE = 199309
__ISO_C_VISIBLE = 1990
__POSIX_VISIBLE = 199209
__ISO_C_VISIBLE = 1990
__POSIX_VISIBLE = 199009
__ISO_C_VISIBLE = 1990
__POSIX_VISIBLE = 198808
__ISO_C_VISIBLE = 0
__POSIX_VISIBLE = 0
__XSI_VISIBLE = 0
__BSD_VISIBLE = 0
__ISO_C_VISIBLE = 1990
__POSIX_VISIBLE = 0
__XSI_VISIBLE = 0
__BSD_VISIBLE = 0
__ISO_C_VISIBLE = 1999
__POSIX_VISIBLE = 200112
__XSI_VISIBLE = 600
__BSD_VISIBLE = 1
__ISO_C_VISIBLE = 1999
_QUAD_HIGHWORD = 1
_QUAD_LOWWORD = 0
_LITTLE_ENDIAN = 1234
_BIG_ENDIAN = 4321
_PDP_ENDIAN = 3412
_BYTE_ORDER = _LITTLE_ENDIAN
LITTLE_ENDIAN = _LITTLE_ENDIAN
BIG_ENDIAN = _BIG_ENDIAN
PDP_ENDIAN = _PDP_ENDIAN
BYTE_ORDER = _BYTE_ORDER

def __word_swap_int_var(x):
    pass


def __word_swap_int_const(x):
    pass


def __word_swap_int(x):
    return __word_swap_int_var(x)


def __byte_swap_int_var(x):
    pass


def __byte_swap_int_const(x):
    pass


def __byte_swap_int(x):
    return __byte_swap_int_var(x)


def __byte_swap_long_var(x):
    pass


def __byte_swap_long_const(x):
    pass


def __byte_swap_long(x):
    return __byte_swap_long_var(x)


def __byte_swap_word_var(x):
    pass


def __byte_swap_word_const(x):
    pass


def __byte_swap_word(x):
    return __byte_swap_word_var(x)


def __htonl(x):
    return __bswap32(x)


def __htons(x):
    return __bswap16(x)


def __ntohl(x):
    return __bswap32(x)


def __ntohs(x):
    return __bswap16(x)


IPPROTO_IP = 0
IPPROTO_ICMP = 1
IPPROTO_TCP = 6
IPPROTO_UDP = 17

def htonl(x):
    return __htonl(x)


def htons(x):
    return __htons(x)


def ntohl(x):
    return __ntohl(x)


def ntohs(x):
    return __ntohs(x)


IPPROTO_RAW = 255
INET_ADDRSTRLEN = 16
IPPROTO_HOPOPTS = 0
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
IPPROTO_IPV4 = 4
IPPROTO_IPIP = IPPROTO_IPV4
IPPROTO_ST = 7
IPPROTO_EGP = 8
IPPROTO_PIGP = 9
IPPROTO_RCCMON = 10
IPPROTO_NVPII = 11
IPPROTO_PUP = 12
IPPROTO_ARGUS = 13
IPPROTO_EMCON = 14
IPPROTO_XNET = 15
IPPROTO_CHAOS = 16
IPPROTO_MUX = 18
IPPROTO_MEAS = 19
IPPROTO_HMP = 20
IPPROTO_PRM = 21
IPPROTO_IDP = 22
IPPROTO_TRUNK1 = 23
IPPROTO_TRUNK2 = 24
IPPROTO_LEAF1 = 25
IPPROTO_LEAF2 = 26
IPPROTO_RDP = 27
IPPROTO_IRTP = 28
IPPROTO_TP = 29
IPPROTO_BLT = 30
IPPROTO_NSP = 31
IPPROTO_INP = 32
IPPROTO_SEP = 33
IPPROTO_3PC = 34
IPPROTO_IDPR = 35
IPPROTO_XTP = 36
IPPROTO_DDP = 37
IPPROTO_CMTP = 38
IPPROTO_TPXX = 39
IPPROTO_IL = 40
IPPROTO_IPV6 = 41
IPPROTO_SDRP = 42
IPPROTO_ROUTING = 43
IPPROTO_FRAGMENT = 44
IPPROTO_IDRP = 45
IPPROTO_RSVP = 46
IPPROTO_GRE = 47
IPPROTO_MHRP = 48
IPPROTO_BHA = 49
IPPROTO_ESP = 50
IPPROTO_AH = 51
IPPROTO_INLSP = 52
IPPROTO_SWIPE = 53
IPPROTO_NHRP = 54
IPPROTO_MOBILE = 55
IPPROTO_TLSP = 56
IPPROTO_SKIP = 57
IPPROTO_ICMPV6 = 58
IPPROTO_NONE = 59
IPPROTO_DSTOPTS = 60
IPPROTO_AHIP = 61
IPPROTO_CFTP = 62
IPPROTO_HELLO = 63
IPPROTO_SATEXPAK = 64
IPPROTO_KRYPTOLAN = 65
IPPROTO_RVD = 66
IPPROTO_IPPC = 67
IPPROTO_ADFS = 68
IPPROTO_SATMON = 69
IPPROTO_VISA = 70
IPPROTO_IPCV = 71
IPPROTO_CPNX = 72
IPPROTO_CPHB = 73
IPPROTO_WSN = 74
IPPROTO_PVP = 75
IPPROTO_BRSATMON = 76
IPPROTO_ND = 77
IPPROTO_WBMON = 78
IPPROTO_WBEXPAK = 79
IPPROTO_EON = 80
IPPROTO_VMTP = 81
IPPROTO_SVMTP = 82
IPPROTO_VINES = 83
IPPROTO_TTP = 84
IPPROTO_IGP = 85
IPPROTO_DGP = 86
IPPROTO_TCF = 87
IPPROTO_IGRP = 88
IPPROTO_OSPFIGP = 89
IPPROTO_SRPC = 90
IPPROTO_LARP = 91
IPPROTO_MTP = 92
IPPROTO_AX25 = 93
IPPROTO_IPEIP = 94
IPPROTO_MICP = 95
IPPROTO_SCCSP = 96
IPPROTO_ETHERIP = 97
IPPROTO_ENCAP = 98
IPPROTO_APES = 99
IPPROTO_GMTP = 100
IPPROTO_IPCOMP = 108
IPPROTO_SCTP = 132
IPPROTO_PIM = 103
IPPROTO_CARP = 112
IPPROTO_PGM = 113
IPPROTO_PFSYNC = 240
IPPROTO_OLD_DIVERT = 254
IPPROTO_MAX = 256
IPPROTO_DONE = 257
IPPROTO_DIVERT = 258
IPPROTO_SPACER = 32767
IPPORT_RESERVED = 1024
IPPORT_HIFIRSTAUTO = 49152
IPPORT_HILASTAUTO = 65535
IPPORT_RESERVEDSTART = 600
IPPORT_MAX = 65535

def IN_CLASSA(i):
    return u_int32_t(i) & 2147483648 == 0


IN_CLASSA_NET = 4278190080
IN_CLASSA_NSHIFT = 24
IN_CLASSA_HOST = 16777215
IN_CLASSA_MAX = 128

def IN_CLASSB(i):
    return u_int32_t(i) & 3221225472 == 2147483648


IN_CLASSB_NET = 4294901760
IN_CLASSB_NSHIFT = 16
IN_CLASSB_HOST = 65535
IN_CLASSB_MAX = 65536

def IN_CLASSC(i):
    return u_int32_t(i) & 3758096384 == 3221225472


IN_CLASSC_NET = 4294967040
IN_CLASSC_NSHIFT = 8
IN_CLASSC_HOST = 255

def IN_CLASSD(i):
    return u_int32_t(i) & 4026531840 == 3758096384


IN_CLASSD_NET = 4026531840
IN_CLASSD_NSHIFT = 28
IN_CLASSD_HOST = 268435455

def IN_MULTICAST(i):
    return IN_CLASSD(i)


def IN_EXPERIMENTAL(i):
    return u_int32_t(i) & 4026531840 == 4026531840


def IN_BADCLASS(i):
    return u_int32_t(i) & 4026531840 == 4026531840


INADDR_NONE = 4294967295
IN_LOOPBACKNET = 127
IP_OPTIONS = 1
IP_HDRINCL = 2
IP_TOS = 3
IP_TTL = 4
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RECVDSTADDR = 7
IP_SENDSRCADDR = IP_RECVDSTADDR
IP_RETOPTS = 8
IP_MULTICAST_IF = 9
IP_MULTICAST_TTL = 10
IP_MULTICAST_LOOP = 11
IP_ADD_MEMBERSHIP = 12
IP_DROP_MEMBERSHIP = 13
IP_MULTICAST_VIF = 14
IP_RSVP_ON = 15
IP_RSVP_OFF = 16
IP_RSVP_VIF_ON = 17
IP_RSVP_VIF_OFF = 18
IP_PORTRANGE = 19
IP_RECVIF = 20
IP_IPSEC_POLICY = 21
IP_FAITH = 22
IP_ONESBCAST = 23
IP_FW_TABLE_ADD = 40
IP_FW_TABLE_DEL = 41
IP_FW_TABLE_FLUSH = 42
IP_FW_TABLE_GETSIZE = 43
IP_FW_TABLE_LIST = 44
IP_FW_ADD = 50
IP_FW_DEL = 51
IP_FW_FLUSH = 52
IP_FW_ZERO = 53
IP_FW_GET = 54
IP_FW_RESETLOG = 55
IP_DUMMYNET_CONFIGURE = 60
IP_DUMMYNET_DEL = 61
IP_DUMMYNET_FLUSH = 62
IP_DUMMYNET_GET = 64
IP_RECVTTL = 65
IP_MINTTL = 66
IP_DONTFRAG = 67
IP_DEFAULT_MULTICAST_TTL = 1
IP_DEFAULT_MULTICAST_LOOP = 1
IP_MAX_MEMBERSHIPS = 20
IP_PORTRANGE_DEFAULT = 0
IP_PORTRANGE_HIGH = 1
IP_PORTRANGE_LOW = 2
IPPROTO_MAXID = IPPROTO_AH + 1
IPCTL_FORWARDING = 1
IPCTL_SENDREDIRECTS = 2
IPCTL_DEFTTL = 3
IPCTL_DEFMTU = 4
IPCTL_RTEXPIRE = 5
IPCTL_RTMINEXPIRE = 6
IPCTL_RTMAXCACHE = 7
IPCTL_SOURCEROUTE = 8
IPCTL_DIRECTEDBROADCAST = 9
IPCTL_INTRQMAXLEN = 10
IPCTL_INTRQDROPS = 11
IPCTL_STATS = 12
IPCTL_ACCEPTSOURCEROUTE = 13
IPCTL_FASTFORWARDING = 14
IPCTL_KEEPFAITH = 15
IPCTL_GIF_TTL = 16
IPCTL_MAXID = 17

def in_nullhost(x):
    return x.s_addr == INADDR_ANY


__KAME_VERSION = 'FreeBSD'
IPV6PORT_RESERVED = 1024
IPV6PORT_ANONMIN = 49152
IPV6PORT_ANONMAX = 65535
IPV6PORT_RESERVEDMIN = 600
IPV6PORT_RESERVEDMAX = IPV6PORT_RESERVED - 1
INET6_ADDRSTRLEN = 46
IPV6_ADDR_INT32_ONE = 1
IPV6_ADDR_INT32_TWO = 2
IPV6_ADDR_INT32_MNL = 4278255616
IPV6_ADDR_INT32_MLL = 4278321152
IPV6_ADDR_INT32_SMP = 65535
IPV6_ADDR_INT16_ULL = 65152
IPV6_ADDR_INT16_USL = 65216
IPV6_ADDR_INT16_MLL = 65282
IPV6_ADDR_INT32_ONE = 16777216
IPV6_ADDR_INT32_TWO = 33554432
IPV6_ADDR_INT32_MNL = 511
IPV6_ADDR_INT32_MLL = 767
IPV6_ADDR_INT32_SMP = 4294901760
IPV6_ADDR_INT16_ULL = 33022
IPV6_ADDR_INT16_USL = 49406
IPV6_ADDR_INT16_MLL = 767

def IN6_IS_ADDR_UNSPECIFIED(a):
    pass


def IN6_IS_ADDR_LOOPBACK(a):
    pass


def IN6_IS_ADDR_V4COMPAT(a):
    pass


def IN6_IS_ADDR_V4MAPPED(a):
    pass


IPV6_ADDR_SCOPE_NODELOCAL = 1
IPV6_ADDR_SCOPE_INTFACELOCAL = 1
IPV6_ADDR_SCOPE_LINKLOCAL = 2
IPV6_ADDR_SCOPE_SITELOCAL = 5
IPV6_ADDR_SCOPE_ORGLOCAL = 8
IPV6_ADDR_SCOPE_GLOBAL = 14
__IPV6_ADDR_SCOPE_NODELOCAL = 1
__IPV6_ADDR_SCOPE_INTFACELOCAL = 1
__IPV6_ADDR_SCOPE_LINKLOCAL = 2
__IPV6_ADDR_SCOPE_SITELOCAL = 5
__IPV6_ADDR_SCOPE_ORGLOCAL = 8
__IPV6_ADDR_SCOPE_GLOBAL = 14

def IN6_IS_ADDR_LINKLOCAL(a):
    pass


def IN6_IS_ADDR_SITELOCAL(a):
    pass


def IN6_IS_ADDR_MC_NODELOCAL(a):
    pass


def IN6_IS_ADDR_MC_INTFACELOCAL(a):
    pass


def IN6_IS_ADDR_MC_LINKLOCAL(a):
    pass


def IN6_IS_ADDR_MC_SITELOCAL(a):
    pass


def IN6_IS_ADDR_MC_ORGLOCAL(a):
    pass


def IN6_IS_ADDR_MC_GLOBAL(a):
    pass


def IN6_IS_ADDR_MC_NODELOCAL(a):
    pass


def IN6_IS_ADDR_MC_LINKLOCAL(a):
    pass


def IN6_IS_ADDR_MC_SITELOCAL(a):
    pass


def IN6_IS_ADDR_MC_ORGLOCAL(a):
    pass


def IN6_IS_ADDR_MC_GLOBAL(a):
    pass


def IN6_IS_SCOPE_LINKLOCAL(a):
    pass


def IFA6_IS_DEPRECATED(a):
    pass


def IFA6_IS_INVALID(a):
    pass


IPV6_OPTIONS = 1
IPV6_RECVOPTS = 5
IPV6_RECVRETOPTS = 6
IPV6_RECVDSTADDR = 7
IPV6_RETOPTS = 8
IPV6_SOCKOPT_RESERVED1 = 3
IPV6_UNICAST_HOPS = 4
IPV6_MULTICAST_IF = 9
IPV6_MULTICAST_HOPS = 10
IPV6_MULTICAST_LOOP = 11
IPV6_JOIN_GROUP = 12
IPV6_LEAVE_GROUP = 13
IPV6_PORTRANGE = 14
ICMP6_FILTER = 18
IPV6_2292PKTINFO = 19
IPV6_2292HOPLIMIT = 20
IPV6_2292NEXTHOP = 21
IPV6_2292HOPOPTS = 22
IPV6_2292DSTOPTS = 23
IPV6_2292RTHDR = 24
IPV6_2292PKTOPTIONS = 25
IPV6_CHECKSUM = 26
IPV6_V6ONLY = 27
IPV6_BINDV6ONLY = IPV6_V6ONLY
IPV6_IPSEC_POLICY = 28
IPV6_FAITH = 29
IPV6_FW_ADD = 30
IPV6_FW_DEL = 31
IPV6_FW_FLUSH = 32
IPV6_FW_ZERO = 33
IPV6_FW_GET = 34
IPV6_RTHDRDSTOPTS = 35
IPV6_RECVPKTINFO = 36
IPV6_RECVHOPLIMIT = 37
IPV6_RECVRTHDR = 38
IPV6_RECVHOPOPTS = 39
IPV6_RECVDSTOPTS = 40
IPV6_RECVRTHDRDSTOPTS = 41
IPV6_USE_MIN_MTU = 42
IPV6_RECVPATHMTU = 43
IPV6_PATHMTU = 44
IPV6_REACHCONF = 45
IPV6_PKTINFO = 46
IPV6_HOPLIMIT = 47
IPV6_NEXTHOP = 48
IPV6_HOPOPTS = 49
IPV6_DSTOPTS = 50
IPV6_RTHDR = 51
IPV6_PKTOPTIONS = 52
IPV6_RECVTCLASS = 57
IPV6_AUTOFLOWLABEL = 59
IPV6_TCLASS = 61
IPV6_DONTFRAG = 62
IPV6_PREFER_TEMPADDR = 63
IPV6_RTHDR_LOOSE = 0
IPV6_RTHDR_STRICT = 1
IPV6_RTHDR_TYPE_0 = 0
IPV6_DEFAULT_MULTICAST_HOPS = 1
IPV6_DEFAULT_MULTICAST_LOOP = 1
IPV6_PORTRANGE_DEFAULT = 0
IPV6_PORTRANGE_HIGH = 1
IPV6_PORTRANGE_LOW = 2
IPV6PROTO_MAXID = IPPROTO_PIM + 1
IPV6CTL_FORWARDING = 1
IPV6CTL_SENDREDIRECTS = 2
IPV6CTL_DEFHLIM = 3
IPV6CTL_DEFMTU = 4
IPV6CTL_FORWSRCRT = 5
IPV6CTL_STATS = 6
IPV6CTL_MRTSTATS = 7
IPV6CTL_MRTPROTO = 8
IPV6CTL_MAXFRAGPACKETS = 9
IPV6CTL_SOURCECHECK = 10
IPV6CTL_SOURCECHECK_LOGINT = 11
IPV6CTL_ACCEPT_RTADV = 12
IPV6CTL_KEEPFAITH = 13
IPV6CTL_LOG_INTERVAL = 14
IPV6CTL_HDRNESTLIMIT = 15
IPV6CTL_DAD_COUNT = 16
IPV6CTL_AUTO_FLOWLABEL = 17
IPV6CTL_DEFMCASTHLIM = 18
IPV6CTL_GIF_HLIM = 19
IPV6CTL_KAME_VERSION = 20
IPV6CTL_USE_DEPRECATED = 21
IPV6CTL_RR_PRUNE = 22
IPV6CTL_MAPPED_ADDR = 23
IPV6CTL_V6ONLY = 24
IPV6CTL_RTEXPIRE = 25
IPV6CTL_RTMINEXPIRE = 26
IPV6CTL_RTMAXCACHE = 27
IPV6CTL_USETEMPADDR = 32
IPV6CTL_TEMPPLTIME = 33
IPV6CTL_TEMPVLTIME = 34
IPV6CTL_AUTO_LINKLOCAL = 35
IPV6CTL_RIP6STATS = 36
IPV6CTL_PREFER_TEMPADDR = 37
IPV6CTL_ADDRCTLPOLICY = 38
IPV6CTL_USE_DEFAULTZONE = 39
IPV6CTL_MAXFRAGS = 41
IPV6CTL_IFQ = 42
IPV6CTL_ISATAPRTR = 43
IPV6CTL_MCAST_PMTU = 44
IPV6CTL_STEALTH = 45
IPV6CTL_MAXID = 46