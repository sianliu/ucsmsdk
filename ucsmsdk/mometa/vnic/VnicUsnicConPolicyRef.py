"""This module contains the general information for VnicUsnicConPolicyRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicUsnicConPolicyRefConsts():
    pass


class VnicUsnicConPolicyRef(ManagedObject):
    """This is VnicUsnicConPolicyRef class."""

    consts = VnicUsnicConPolicyRefConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicUsnicConPolicyRef", "vnicUsnicConPolicyRef", "usnic-con-ref", VersionMeta.Version221b, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], [u'vnicEther', u'vnicLanConnTempl'], [u'faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "oper_con_policy_name": MoPropertyMeta("oper_con_policy_name", "operConPolicyName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "operConPolicyName": "oper_con_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.con_policy_name = None
        self.oper_con_policy_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicUsnicConPolicyRef", parent_mo_or_dn, **kwargs)

