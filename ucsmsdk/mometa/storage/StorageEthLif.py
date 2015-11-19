"""This module contains the general information for StorageEthLif ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageEthLifConsts():
    DEFAULT_NET_FALSE = "false"
    DEFAULT_NET_NO = "no"
    DEFAULT_NET_TRUE = "true"
    DEFAULT_NET_YES = "yes"
    OPER_STATE_DOWN = "down"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_UP = "up"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    SHARING_COMMUNITY = "community"
    SHARING_ISOLATED = "isolated"
    SHARING_NONE = "none"
    SHARING_PRIMARY = "primary"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"


class StorageEthLif(ManagedObject):
    """This is StorageEthLif class."""

    consts = StorageEthLifConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("StorageEthLif", "storageEthLif", "eth-lif-[name]", VersionMeta.Version302a, "InputOutput", 0x1fL, [], ["read-only"], [u'osInstance', u'storageProcessor'], [u'osEthBondIntf', u'osEthIntf', u'vnicIPv4If'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-vxlan-vmq|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig),){0,50}(defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-vxlan-vmq|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig){0,1}""", [], []), 
        "default_net": MoPropertyMeta("default_net", "defaultNet", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "failed", "indeterminate", "up"], []), 
        "oper_vnet_dn": MoPropertyMeta("oper_vnet_dn", "operVnetDn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vnet_name": MoPropertyMeta("oper_vnet_name", "operVnetName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []), 
        "pub_nw_id": MoPropertyMeta("pub_nw_id", "pubNwId", "uint", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|none|nfs|node-mgmt|node-ha-state|cifs|data-protection|iscsi),){0,7}(defaultValue|none|nfs|node-mgmt|node-ha-state|cifs|data-protection|iscsi){0,1}""", [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sharing": MoPropertyMeta("sharing", "sharing", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["community", "isolated", "none", "primary"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []), 
        "vnet": MoPropertyMeta("vnet", "vnet", "uint", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "defaultNet": "default_net", 
        "dn": "dn", 
        "name": "name", 
        "operState": "oper_state", 
        "operVnetDn": "oper_vnet_dn", 
        "operVnetName": "oper_vnet_name", 
        "owner": "owner", 
        "pubNwId": "pub_nw_id", 
        "rn": "rn", 
        "role": "role", 
        "sacl": "sacl", 
        "sharing": "sharing", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
        "vnet": "vnet", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_qualifier = None
        self.default_net = None
        self.oper_state = None
        self.oper_vnet_dn = None
        self.oper_vnet_name = None
        self.owner = None
        self.pub_nw_id = None
        self.role = None
        self.sacl = None
        self.sharing = None
        self.status = None
        self.switch_id = None
        self.type = None
        self.vnet = None

        ManagedObject.__init__(self, "StorageEthLif", parent_mo_or_dn, **kwargs)

