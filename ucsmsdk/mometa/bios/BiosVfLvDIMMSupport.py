"""This module contains the general information for BiosVfLvDIMMSupport ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfLvDIMMSupportConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_LV_DDRMODE_AUTO = "auto"
    VP_LV_DDRMODE_PERFORMANCE_MODE = "performance-mode"
    VP_LV_DDRMODE_PLATFORM_DEFAULT = "platform-default"
    VP_LV_DDRMODE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_LV_DDRMODE_POWER_SAVING_MODE = "power-saving-mode"


class BiosVfLvDIMMSupport(ManagedObject):
    """This is BiosVfLvDIMMSupport class."""

    consts = BiosVfLvDIMMSupportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfLvDIMMSupport", "biosVfLvDIMMSupport", "LvDIMM-Support", VersionMeta.Version131c, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_lv_ddr_mode": MoPropertyMeta("vp_lv_ddr_mode", "vpLvDDRMode", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["auto", "performance-mode", "platform-default", "platform-recommended", "power-saving-mode"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpLvDDRMode": "vp_lv_ddr_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_lv_ddr_mode = None

        ManagedObject.__init__(self, "BiosVfLvDIMMSupport", parent_mo_or_dn, **kwargs)

