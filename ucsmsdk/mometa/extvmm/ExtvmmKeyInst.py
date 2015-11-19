"""This module contains the general information for ExtvmmKeyInst ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ExtvmmKeyInstConsts():
    pass


class ExtvmmKeyInst(ManagedObject):
    """This is ExtvmmKeyInst class."""

    consts = ExtvmmKeyInstConsts()
    naming_props = set([u'inst'])

    mo_meta = MoMeta("ExtvmmKeyInst", "extvmmKeyInst", "key-[inst]", VersionMeta.Version111j, "InputOutput", 0x1fL, [], ["read-only"], [u'extvmmProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "inst": MoPropertyMeta("inst", "inst", "ushort", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], []), 
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 1, 33, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "inst": "inst", 
        "key": "key", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, inst, **kwargs):
        self._dirty_mask = 0
        self.inst = inst
        self.child_action = None
        self.key = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtvmmKeyInst", parent_mo_or_dn, **kwargs)

