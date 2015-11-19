"""This module contains the general information for EquipmentBladeSwitchConnDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentBladeSwitchConnDefConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PORT_BANDWIDTH_10GBPS = "10gbps"
    PORT_BANDWIDTH_1GBPS = "1gbps"
    PORT_BANDWIDTH_20GBPS = "20gbps"
    PORT_BANDWIDTH_40GBPS = "40gbps"
    PORT_BANDWIDTH_INDETERMINATE = "indeterminate"


class EquipmentBladeSwitchConnDef(ManagedObject):
    """This is EquipmentBladeSwitchConnDef class."""

    consts = EquipmentBladeSwitchConnDefConsts()
    naming_props = set([u'switchType'])

    mo_meta = MoMeta("EquipmentBladeSwitchConnDef", "equipmentBladeSwitchConnDef", "-switch-type-[switch_type]", VersionMeta.Version302a, "InputOutput", 0xffL, [], [""], [u'equipmentBladeConnDef'], [u'equipmentAdaptorConnDef'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "port_bandwidth": MoPropertyMeta("port_bandwidth", "portBandwidth", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10gbps", "1gbps", "20gbps", "40gbps", "indeterminate"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_type": MoPropertyMeta("switch_type", "switchType", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x80L, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "portBandwidth": "port_bandwidth", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchType": "switch_type", 
    }

    def __init__(self, parent_mo_or_dn, switch_type, **kwargs):
        self._dirty_mask = 0
        self.switch_type = switch_type
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.port_bandwidth = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBladeSwitchConnDef", parent_mo_or_dn, **kwargs)

