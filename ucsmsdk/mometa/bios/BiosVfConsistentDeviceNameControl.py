"""This module contains the general information for BiosVfConsistentDeviceNameControl ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfConsistentDeviceNameControlConsts():
    VP_CDNCONTROL_DISABLED = "disabled"
    VP_CDNCONTROL_ENABLED = "enabled"
    VP_CDNCONTROL_PLATFORM_DEFAULT = "platform-default"
    VP_CDNCONTROL_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfConsistentDeviceNameControl(ManagedObject):
    """This is BiosVfConsistentDeviceNameControl class."""

    consts = BiosVfConsistentDeviceNameControlConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfConsistentDeviceNameControl", "biosVfConsistentDeviceNameControl", "Consistent-Device-Name-Control", VersionMeta.Version224a, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vp_cdn_control": MoPropertyMeta("vp_cdn_control", "vpCDNControl", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpCDNControl": "vp_cdn_control", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cdn_control = None

        ManagedObject.__init__(self, "BiosVfConsistentDeviceNameControl", parent_mo_or_dn, **kwargs)

