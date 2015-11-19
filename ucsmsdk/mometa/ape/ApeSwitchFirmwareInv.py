"""This module contains the general information for ApeSwitchFirmwareInv ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeSwitchFirmwareInvConsts():
    FABRIC_A = "A"
    FABRIC_B = "B"
    FABRIC_NONE = "NONE"


class ApeSwitchFirmwareInv(ManagedObject):
    """This is ApeSwitchFirmwareInv class."""

    consts = ApeSwitchFirmwareInvConsts()
    naming_props = set([u'fabric'])

    mo_meta = MoMeta("ApeSwitchFirmwareInv", "apeSwitchFirmwareInv", "SwitchFirmwareInv-[fabric]", VersionMeta.Version131c, "InputOutput", 0x7ffL, [], ["read-only"], [u'apeDcosAgManager'], [], [None])

    prop_meta = {
        "bios_version": MoPropertyMeta("bios_version", "biosVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "fabric": MoPropertyMeta("fabric", "fabric", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x8L, None, None, None, ["A", "B", "NONE"], []), 
        "ks_startup_version": MoPropertyMeta("ks_startup_version", "ksStartupVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10L, 0, 510, None, [], []), 
        "ks_version": MoPropertyMeta("ks_version", "ksVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_startup_version": MoPropertyMeta("sys_startup_version", "sysStartupVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x200L, 0, 510, None, [], []), 
        "sys_version": MoPropertyMeta("sys_version", "sysVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x400L, 0, 510, None, [], []), 
    }

    prop_map = {
        "biosVersion": "bios_version", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fabric": "fabric", 
        "ksStartupVersion": "ks_startup_version", 
        "ksVersion": "ks_version", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "sysStartupVersion": "sys_startup_version", 
        "sysVersion": "sys_version", 
    }

    def __init__(self, parent_mo_or_dn, fabric, **kwargs):
        self._dirty_mask = 0
        self.fabric = fabric
        self.bios_version = None
        self.child_action = None
        self.ks_startup_version = None
        self.ks_version = None
        self.name = None
        self.sacl = None
        self.status = None
        self.sys_startup_version = None
        self.sys_version = None

        ManagedObject.__init__(self, "ApeSwitchFirmwareInv", parent_mo_or_dn, **kwargs)

