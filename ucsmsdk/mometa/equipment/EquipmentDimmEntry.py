"""This module contains the general information for EquipmentDimmEntry ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentDimmEntryConsts():
    pass


class EquipmentDimmEntry(ManagedObject):
    """This is EquipmentDimmEntry class."""

    consts = EquipmentDimmEntryConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("EquipmentDimmEntry", "equipmentDimmEntry", "dimm-entry[id]", VersionMeta.Version202m, "InputOutput", 0x1fL, [], [""], [u'equipmentDimmMapping'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version202m, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "smbiosname": MoPropertyMeta("smbiosname", "smbiosname", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "smbiosname": "smbiosname", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.sacl = None
        self.smbiosname = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentDimmEntry", parent_mo_or_dn, **kwargs)

