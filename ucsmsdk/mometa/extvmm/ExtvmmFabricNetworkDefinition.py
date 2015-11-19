"""This module contains the general information for ExtvmmFabricNetworkDefinition ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ExtvmmFabricNetworkDefinitionConsts():
    ALLOWED_VNIC_TYPE_ETHER = "ether"
    ALLOWED_VNIC_TYPE_FC = "fc"
    ALLOWED_VNIC_TYPE_IPC = "ipc"
    ALLOWED_VNIC_TYPE_SCSI = "scsi"
    ALLOWED_VNIC_TYPE_UNKNOWN = "unknown"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REF_OPER_STATE_INVALID_REFERENCE = "invalid-reference"
    REF_OPER_STATE_UP = "up"


class ExtvmmFabricNetworkDefinition(ManagedObject):
    """This is ExtvmmFabricNetworkDefinition class."""

    consts = ExtvmmFabricNetworkDefinitionConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ExtvmmFabricNetworkDefinition", "extvmmFabricNetworkDefinition", "fabric-network-def-[name]", VersionMeta.Version221b, "InputOutput", 0x1ffL, [], ["admin", "ls-network", "ls-network-policy"], [u'extvmmFabricNetwork'], [u'extvmmVMNetworkDefinition'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "allowed_vnic_type": MoPropertyMeta("allowed_vnic_type", "allowedVnicType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "primary_vlan_id": MoPropertyMeta("primary_vlan_id", "primaryVlanId", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]), 
        "ref_oper_state": MoPropertyMeta("ref_oper_state", "refOperState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["invalid-reference", "up"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "allowedVnicType": "allowed_vnic_type", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "guid": "guid", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "primaryVlanId": "primary_vlan_id", 
        "refOperState": "ref_oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.allowed_vnic_type = None
        self.child_action = None
        self.descr = None
        self.guid = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.primary_vlan_id = None
        self.ref_oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtvmmFabricNetworkDefinition", parent_mo_or_dn, **kwargs)

