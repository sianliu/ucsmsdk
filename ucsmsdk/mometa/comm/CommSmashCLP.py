"""This module contains the general information for CommSmashCLP ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CommSmashCLPConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommSmashCLP(ManagedObject):
    """This is CommSmashCLP class."""

    consts = CommSmashCLPConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommSmashCLP", "commSmashCLP", "smashclp-svc", VersionMeta.Version101e, "InputOutput", 0xffL, [], ["aaa", "admin"], [u'commSvcEp'], [], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_port": MoPropertyMeta("oper_port", "operPort", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["0-65535"]), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operPort": "oper_port", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "port": "port", 
        "proto": "proto", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.oper_port = None
        self.policy_level = None
        self.policy_owner = None
        self.port = None
        self.proto = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CommSmashCLP", parent_mo_or_dn, **kwargs)

