"""This module contains the general information for BiosVfPackageCStateLimit ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfPackageCStateLimitConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PACKAGE_CSTATE_LIMIT_AUTO = "auto"
    VP_PACKAGE_CSTATE_LIMIT_C0 = "c0"
    VP_PACKAGE_CSTATE_LIMIT_C1 = "c1"
    VP_PACKAGE_CSTATE_LIMIT_C2 = "c2"
    VP_PACKAGE_CSTATE_LIMIT_C3 = "c3"
    VP_PACKAGE_CSTATE_LIMIT_C6 = "c6"
    VP_PACKAGE_CSTATE_LIMIT_C7 = "c7"
    VP_PACKAGE_CSTATE_LIMIT_C7S = "c7s"
    VP_PACKAGE_CSTATE_LIMIT_NO_LIMIT = "no-limit"
    VP_PACKAGE_CSTATE_LIMIT_PLATFORM_DEFAULT = "platform-default"
    VP_PACKAGE_CSTATE_LIMIT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfPackageCStateLimit(ManagedObject):
    """This is BiosVfPackageCStateLimit class."""

    consts = BiosVfPackageCStateLimitConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfPackageCStateLimit", "biosVfPackageCStateLimit", "Package-C-State-Limit", VersionMeta.Version202m, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_package_c_state_limit": MoPropertyMeta("vp_package_c_state_limit", "vpPackageCStateLimit", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["auto", "c0", "c1", "c2", "c3", "c6", "c7", "c7s", "no-limit", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpPackageCStateLimit": "vp_package_c_state_limit", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_package_c_state_limit = None

        ManagedObject.__init__(self, "BiosVfPackageCStateLimit", parent_mo_or_dn, **kwargs)

