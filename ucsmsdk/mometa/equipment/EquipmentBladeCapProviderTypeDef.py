"""This module contains the general information for EquipmentBladeCapProviderTypeDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentBladeCapProviderTypeDefConsts():
    pass


class EquipmentBladeCapProviderTypeDef(ManagedObject):
    """This is EquipmentBladeCapProviderTypeDef class."""

    consts = EquipmentBladeCapProviderTypeDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentBladeCapProviderTypeDef", "equipmentBladeCapProviderTypeDef", "blade-provider-type", VersionMeta.Version224a, "InputOutput", 0x3fL, [], [""], [u'equipmentBladeCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "num_adapter_slots": MoPropertyMeta("num_adapter_slots", "numAdapterSlots", "ushort", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], []), 
        "num_slots": MoPropertyMeta("num_slots", "numSlots", "ushort", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "numAdapterSlots": "num_adapter_slots", 
        "numSlots": "num_slots", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.num_adapter_slots = None
        self.num_slots = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBladeCapProviderTypeDef", parent_mo_or_dn, **kwargs)

