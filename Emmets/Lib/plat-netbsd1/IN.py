# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-netbsd1/IN.py
IPPROTO_IP = 0
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
IPPROTO_IPIP = 4
IPPROTO_TCP = 6
IPPROTO_EGP = 8
IPPROTO_PUP = 12
IPPROTO_UDP = 17
IPPROTO_IDP = 22
IPPROTO_TP = 29
IPPROTO_EON = 80
IPPROTO_ENCAP = 98
IPPROTO_RAW = 255
IPPROTO_MAX = 256
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000

def __IPADDR(x):
    return u_int32_t(x)


IN_CLASSA_NSHIFT = 24
IN_CLASSA_MAX = 128
IN_CLASSB_NSHIFT = 16
IN_CLASSB_MAX = 65536
IN_CLASSC_NSHIFT = 8
IN_CLASSD_NSHIFT = 28

def IN_MULTICAST(i):
    return IN_CLASSD(i)


IN_LOOPBACKNET = 127
IP_OPTIONS = 1
IP_HDRINCL = 2
IP_TOS = 3
IP_TTL = 4
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RECVDSTADDR = 7
IP_RETOPTS = 8
IP_MULTICAST_IF = 9
IP_MULTICAST_TTL = 10
IP_MULTICAST_LOOP = 11
IP_ADD_MEMBERSHIP = 12
IP_DROP_MEMBERSHIP = 13
IP_RECVIF = 20
IP_DEFAULT_MULTICAST_TTL = 1
IP_DEFAULT_MULTICAST_LOOP = 1
IP_MAX_MEMBERSHIPS = 20
IPPROTO_MAXID = IPPROTO_IDP + 1
IPCTL_FORWARDING = 1
IPCTL_SENDREDIRECTS = 2
IPCTL_DEFTTL = 3
IPCTL_DEFMTU = 4
IPCTL_FORWSRCRT = 5
IPCTL_DIRECTEDBCAST = 6
IPCTL_ALLOWSRCRT = 7
IPCTL_MAXID = 8

def in_nullhost(x):
    return x.s_addr == INADDR_ANY