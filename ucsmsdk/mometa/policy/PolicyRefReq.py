"""This module contains the general information for PolicyRefReq ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class PolicyRefReqConsts():
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class PolicyRefReq(ManagedObject):
    """This is PolicyRefReq class."""

    consts = PolicyRefReqConsts()
    naming_props = set([u'refConvertedDn'])

    mo_meta = MoMeta("PolicyRefReq", "policyRefReq", "refreq-[ref_converted_dn]", VersionMeta.Version212a, "InputOutput", 0x1fL, [], ["admin"], [u'policyElement'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy"], []), 
        "ref_converted_dn": MoPropertyMeta("ref_converted_dn", "refConvertedDn", "string", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x4L, 1, 510, None, [], []), 
        "ref_policy_dn": MoPropertyMeta("ref_policy_dn", "refPolicyDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "policyOwner": "policy_owner", 
        "refConvertedDn": "ref_converted_dn", 
        "refPolicyDn": "ref_policy_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, ref_converted_dn, **kwargs):
        self._dirty_mask = 0
        self.ref_converted_dn = ref_converted_dn
        self.child_action = None
        self.policy_owner = None
        self.ref_policy_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyRefReq", parent_mo_or_dn, **kwargs)

