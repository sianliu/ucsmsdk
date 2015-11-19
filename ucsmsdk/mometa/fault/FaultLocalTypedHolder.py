"""This module contains the general information for FaultLocalTypedHolder ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FaultLocalTypedHolderConsts():
    TYPE_ANY = "any"
    TYPE_CONFIGURATION = "configuration"
    TYPE_CONNECTIVITY = "connectivity"
    TYPE_ENVIRONMENTAL = "environmental"
    TYPE_EQUIPMENT = "equipment"
    TYPE_FORWARD = "forward"
    TYPE_FSM = "fsm"
    TYPE_GENERIC = "generic"
    TYPE_MANAGEMENT = "management"
    TYPE_NETWORK = "network"
    TYPE_OPERATIONAL = "operational"
    TYPE_SECURITY = "security"
    TYPE_SERVER = "server"
    TYPE_STORAGE = "storage"
    TYPE_SYSDEBUG = "sysdebug"


class FaultLocalTypedHolder(ManagedObject):
    """This is FaultLocalTypedHolder class."""

    consts = FaultLocalTypedHolderConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("FaultLocalTypedHolder", "faultLocalTypedHolder", "type-[type]", VersionMeta.Version211a, "InputOutput", 0x1fL, [], ["admin", "fault"], [u'faultHolder'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_faults": MoPropertyMeta("total_faults", "totalFaults", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x10L, None, None, None, ["any", "configuration", "connectivity", "environmental", "equipment", "forward", "fsm", "generic", "management", "network", "operational", "security", "server", "storage", "sysdebug"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "totalFaults": "total_faults", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.name = None
        self.sacl = None
        self.status = None
        self.total_faults = None

        ManagedObject.__init__(self, "FaultLocalTypedHolder", parent_mo_or_dn, **kwargs)

