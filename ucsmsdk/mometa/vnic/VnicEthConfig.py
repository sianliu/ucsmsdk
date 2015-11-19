"""This module contains the general information for VnicEthConfig ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicEthConfigConsts():
    pass


class VnicEthConfig(ManagedObject):
    """This is VnicEthConfig class."""

    consts = VnicEthConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicEthConfig", "vnicEthConfig", "eth-vnic", VersionMeta.Version302a, "InputOutput", 0xffL, [], ["admin", "ls-config", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], [u'vnicIScsiInitAutoConfigPolicy'], [u'faultInst'], [None])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "mac_pool_name": MoPropertyMeta("mac_pool_name", "macPoolName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "nw_ctrl_policy_name": MoPropertyMeta("nw_ctrl_policy_name", "nwCtrlPolicyName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_adaptor_profile_name": MoPropertyMeta("oper_adaptor_profile_name", "operAdaptorProfileName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_mac_pool_name": MoPropertyMeta("oper_mac_pool_name", "operMacPoolName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_nw_ctrl_policy_name": MoPropertyMeta("oper_nw_ctrl_policy_name", "operNwCtrlPolicyName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "macPoolName": "mac_pool_name", 
        "nwCtrlPolicyName": "nw_ctrl_policy_name", 
        "operAdaptorProfileName": "oper_adaptor_profile_name", 
        "operMacPoolName": "oper_mac_pool_name", 
        "operNwCtrlPolicyName": "oper_nw_ctrl_policy_name", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_profile_name = None
        self.child_action = None
        self.mac_pool_name = None
        self.nw_ctrl_policy_name = None
        self.oper_adaptor_profile_name = None
        self.oper_mac_pool_name = None
        self.oper_nw_ctrl_policy_name = None
        self.oper_stats_policy_name = None
        self.sacl = None
        self.stats_policy_name = None
        self.status = None

        ManagedObject.__init__(self, "VnicEthConfig", parent_mo_or_dn, **kwargs)

