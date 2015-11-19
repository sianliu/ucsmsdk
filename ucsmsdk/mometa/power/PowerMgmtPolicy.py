"""This module contains the general information for PowerMgmtPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class PowerMgmtPolicyConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROFILING_FALSE = "false"
    PROFILING_NO = "no"
    PROFILING_TRUE = "true"
    PROFILING_YES = "yes"
    SKIP_POWER_CHECK_FALSE = "false"
    SKIP_POWER_CHECK_NO = "no"
    SKIP_POWER_CHECK_TRUE = "true"
    SKIP_POWER_CHECK_YES = "yes"
    SKIP_POWER_DEPLOY_CHECK_FALSE = "false"
    SKIP_POWER_DEPLOY_CHECK_NO = "no"
    SKIP_POWER_DEPLOY_CHECK_TRUE = "true"
    SKIP_POWER_DEPLOY_CHECK_YES = "yes"
    STYLE_INTELLIGENT_POLICY_DRIVEN = "intelligent-policy-driven"
    STYLE_MANUAL_PER_BLADE = "manual-per-blade"


class PowerMgmtPolicy(ManagedObject):
    """This is PowerMgmtPolicy class."""

    consts = PowerMgmtPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("PowerMgmtPolicy", "powerMgmtPolicy", "pwr-mgmt-policy", VersionMeta.Version141i, "InputOutput", 0x7ffL, [], ["admin", "power-mgmt"], [u'orgOrg'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "profiling": MoPropertyMeta("profiling", "profiling", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "skip_power_check": MoPropertyMeta("skip_power_check", "skipPowerCheck", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["false", "no", "true", "yes"], []), 
        "skip_power_deploy_check": MoPropertyMeta("skip_power_deploy_check", "skipPowerDeployCheck", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "style": MoPropertyMeta("style", "style", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["intelligent-policy-driven", "manual-per-blade"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "profiling": "profiling", 
        "rn": "rn", 
        "sacl": "sacl", 
        "skipPowerCheck": "skip_power_check", 
        "skipPowerDeployCheck": "skip_power_deploy_check", 
        "status": "status", 
        "style": "style", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.profiling = None
        self.sacl = None
        self.skip_power_check = None
        self.skip_power_deploy_check = None
        self.status = None
        self.style = None

        ManagedObject.__init__(self, "PowerMgmtPolicy", parent_mo_or_dn, **kwargs)

