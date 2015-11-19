"""This module contains the general information for MgmtInbandProfile ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class MgmtInbandProfileConsts():
    pass


class MgmtInbandProfile(ManagedObject):
    """This is MgmtInbandProfile class."""

    consts = MgmtInbandProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtInbandProfile", "mgmtInbandProfile", "ib-profile", VersionMeta.Version221b, "InputOutput", 0x7fL, [], ["admin", "ext-lan-config", "ext-lan-policy"], [u'fabricLanCloud'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "default_vlan_name": MoPropertyMeta("default_vlan_name", "defaultVlanName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "pool_name": MoPropertyMeta("pool_name", "poolName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "defaultVlanName": "default_vlan_name", 
        "dn": "dn", 
        "name": "name", 
        "poolName": "pool_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.default_vlan_name = None
        self.name = None
        self.pool_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtInbandProfile", parent_mo_or_dn, **kwargs)

