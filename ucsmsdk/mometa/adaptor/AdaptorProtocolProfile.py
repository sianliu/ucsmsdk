"""This module contains the general information for AdaptorProtocolProfile ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorProtocolProfileConsts():
    BOOT_TO_TARGET_FALSE = "false"
    BOOT_TO_TARGET_NO = "no"
    BOOT_TO_TARGET_TRUE = "true"
    BOOT_TO_TARGET_YES = "yes"
    HBA_MODE_FALSE = "false"
    HBA_MODE_NO = "no"
    HBA_MODE_TRUE = "true"
    HBA_MODE_YES = "yes"
    TCP_TIME_STAMP_FALSE = "false"
    TCP_TIME_STAMP_NO = "no"
    TCP_TIME_STAMP_TRUE = "true"
    TCP_TIME_STAMP_YES = "yes"


class AdaptorProtocolProfile(ManagedObject):
    """This is AdaptorProtocolProfile class."""

    consts = AdaptorProtocolProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorProtocolProfile", "adaptorProtocolProfile", "iscsi-prot-profile", VersionMeta.Version201m, "InputOutput", 0x3ffL, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], [u'adaptorHostIscsiIf', u'adaptorHostIscsiIfProfile'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "boot_to_target": MoPropertyMeta("boot_to_target", "bootToTarget", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_time_out": MoPropertyMeta("connection_time_out", "connectionTimeOut", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["0-255"]), 
        "dhcp_time_out": MoPropertyMeta("dhcp_time_out", "dhcpTimeOut", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["60-300"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "hba_mode": MoPropertyMeta("hba_mode", "hbaMode", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["false", "no", "true", "yes"], []), 
        "lun_busy_retry_count": MoPropertyMeta("lun_busy_retry_count", "lunBusyRetryCount", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["0-60"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tcp_time_stamp": MoPropertyMeta("tcp_time_stamp", "tcpTimeStamp", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "bootToTarget": "boot_to_target", 
        "childAction": "child_action", 
        "connectionTimeOut": "connection_time_out", 
        "dhcpTimeOut": "dhcp_time_out", 
        "dn": "dn", 
        "hbaMode": "hba_mode", 
        "lunBusyRetryCount": "lun_busy_retry_count", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tcpTimeStamp": "tcp_time_stamp", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.boot_to_target = None
        self.child_action = None
        self.connection_time_out = None
        self.dhcp_time_out = None
        self.hba_mode = None
        self.lun_busy_retry_count = None
        self.sacl = None
        self.status = None
        self.tcp_time_stamp = None

        ManagedObject.__init__(self, "AdaptorProtocolProfile", parent_mo_or_dn, **kwargs)

