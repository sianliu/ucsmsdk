"""This module contains the general information for SyntheticTime ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SyntheticTimeConsts():
    pass


class SyntheticTime(ManagedObject):
    """This is SyntheticTime class."""

    consts = SyntheticTimeConsts()
    naming_props = set([u'ts'])

    mo_meta = MoMeta("SyntheticTime", "syntheticTime", "time-[ts]", VersionMeta.Version101e, "InputOutput", 0x1fL, [], ["admin"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "ts": MoPropertyMeta("ts", "ts", "ulong", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10L, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "ts": "ts", 
    }

    def __init__(self, parent_mo_or_dn, ts, **kwargs):
        self._dirty_mask = 0
        self.ts = ts
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SyntheticTime", parent_mo_or_dn, **kwargs)

