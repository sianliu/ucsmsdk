"""This module contains the general information for StatsCollectionPolicyFsmTask ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StatsCollectionPolicyFsmTaskConsts():
    COMPLETION_CANCELLED = "cancelled"
    COMPLETION_COMPLETED = "completed"
    COMPLETION_PROCESSING = "processing"
    COMPLETION_SCHEDULED = "scheduled"
    ITEM_NOP = "nop"
    ITEM_UPDATE_EP = "updateEp"


class StatsCollectionPolicyFsmTask(ManagedObject):
    """This is StatsCollectionPolicyFsmTask class."""

    consts = StatsCollectionPolicyFsmTaskConsts()
    naming_props = set([u'item'])

    mo_meta = MoMeta("StatsCollectionPolicyFsmTask", "statsCollectionPolicyFsmTask", "task-[item]", VersionMeta.Version111j, "OutputOnly", 0x7L, [], [""], [u'statsCollectionPolicy'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "completion": MoPropertyMeta("completion", "completion", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cancelled", "completed", "processing", "scheduled"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x1L, 0, 256, None, [], []), 
        "flags": MoPropertyMeta("flags", "flags", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, """(defaultValue){0,1}""", [], []), 
        "item": MoPropertyMeta("item", "item", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["nop", "updateEp"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "seq_id": MoPropertyMeta("seq_id", "seqId", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "completion": "completion", 
        "dn": "dn", 
        "flags": "flags", 
        "item": "item", 
        "rn": "rn", 
        "sacl": "sacl", 
        "seqId": "seq_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, item, **kwargs):
        self._dirty_mask = 0
        self.item = item
        self.child_action = None
        self.completion = None
        self.flags = None
        self.sacl = None
        self.seq_id = None
        self.status = None

        ManagedObject.__init__(self, "StatsCollectionPolicyFsmTask", parent_mo_or_dn, **kwargs)

