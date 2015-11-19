"""This module contains the general information for EventEpCtrl ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EventEpCtrlConsts():
    LEVEL_CLEARED = "cleared"
    LEVEL_CONDITION = "condition"
    LEVEL_CRITICAL = "critical"
    LEVEL_INFO = "info"
    LEVEL_MAJOR = "major"
    LEVEL_MINOR = "minor"
    LEVEL_WARNING = "warning"
    REVERT_TIMEOUT_FOREVER = "forever"


class EventEpCtrl(ManagedObject):
    """This is EventEpCtrl class."""

    consts = EventEpCtrlConsts()
    naming_props = set([])

    mo_meta = MoMeta("EventEpCtrl", "eventEpCtrl", "evctrl", VersionMeta.Version101e, "InputOutput", 0x3fL, [], ["admin", "fault", "operations"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "revert_timeout": MoPropertyMeta("revert_timeout", "revertTimeout", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["forever"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "level": "level", 
        "revertTimeout": "revert_timeout", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.level = None
        self.revert_timeout = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EventEpCtrl", parent_mo_or_dn, **kwargs)

