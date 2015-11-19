"""This module contains the general information for EquipmentLocalDiskControllerCapRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentLocalDiskControllerCapRefConsts():
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class EquipmentLocalDiskControllerCapRef(ManagedObject):
    """This is EquipmentLocalDiskControllerCapRef class."""

    consts = EquipmentLocalDiskControllerCapRefConsts()
    naming_props = set([u'vendor', u'model', u'revision'])

    mo_meta = MoMeta("EquipmentLocalDiskControllerCapRef", "equipmentLocalDiskControllerCapRef", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version142b, "InputOutput", 0x7fL, [], [""], [u'equipmentBladeCapProvider', u'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version142b, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version142b, MoPropertyMeta.NAMING, 0x4L, 1, 510, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version142b, MoPropertyMeta.NAMING, 0x8L, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version142b, MoPropertyMeta.NAMING, 0x40L, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSupported": "is_supported", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.is_supported = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentLocalDiskControllerCapRef", parent_mo_or_dn, **kwargs)

