"""This module contains the general information for EquipmentAdaptorConnDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentAdaptorConnDefConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentAdaptorConnDef(ManagedObject):
    """This is EquipmentAdaptorConnDef class."""

    consts = EquipmentAdaptorConnDefConsts()
    naming_props = set([u'adaptorEp', u'iomEp'])

    mo_meta = MoMeta("EquipmentAdaptorConnDef", "equipmentAdaptorConnDef", "adaptor-port-[adaptor_ep]-iom-port-[iom_ep]", VersionMeta.Version202m, "InputOutput", 0x1ffL, [], [""], [u'equipmentBladeIOMConnDef', u'equipmentBladeSwitchConnDef'], [], ["Get"])

    prop_meta = {
        "adaptor_ep": MoPropertyMeta("adaptor_ep", "adaptorEp", "ushort", VersionMeta.Version202m, MoPropertyMeta.NAMING, 0x1L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "iom_ep": MoPropertyMeta("iom_ep", "iomEp", "ushort", VersionMeta.Version202m, MoPropertyMeta.NAMING, 0x10L, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adaptorEp": "adaptor_ep", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "iomEp": "iom_ep", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, adaptor_ep, iom_ep, **kwargs):
        self._dirty_mask = 0
        self.adaptor_ep = adaptor_ep
        self.iom_ep = iom_ep
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentAdaptorConnDef", parent_mo_or_dn, **kwargs)

