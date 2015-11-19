"""This module contains the general information for InitiatorRequestorGrpEp ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class InitiatorRequestorGrpEpConsts():
    ALLOC_STATE_ALLOCATED = "allocated"
    ALLOC_STATE_ALLOCATING = "allocating"
    ALLOC_STATE_FAILED = "failed"
    ALLOC_STATE_NONE = "none"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    TYPE_DEDICATED = "dedicated"
    TYPE_POLICY = "policy"
    TYPE_SHARED = "shared"


class InitiatorRequestorGrpEp(ManagedObject):
    """This is InitiatorRequestorGrpEp class."""

    consts = InitiatorRequestorGrpEpConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("InitiatorRequestorGrpEp", "initiatorRequestorGrpEp", "req-grp-[id]", VersionMeta.Version211a, "InputOutput", 0x1fL, [], ["read-only"], [u'topSystem'], [u'initiatorMemberEp', u'initiatorUnitEp'], [None])

    prop_meta = {
        "alloc_state": MoPropertyMeta("alloc_state", "allocState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "allocating", "failed", "none"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "pol_dn": MoPropertyMeta("pol_dn", "polDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["dedicated", "policy", "shared"], []), 
    }

    prop_map = {
        "allocState": "alloc_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "lc": "lc", 
        "polDn": "pol_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.alloc_state = None
        self.child_action = None
        self.ep_dn = None
        self.lc = None
        self.pol_dn = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "InitiatorRequestorGrpEp", parent_mo_or_dn, **kwargs)

