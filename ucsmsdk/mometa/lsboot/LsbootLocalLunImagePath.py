"""This module contains the general information for LsbootLocalLunImagePath ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LsbootLocalLunImagePathConsts():
    TYPE_PRIMARY = "primary"
    TYPE_SECONDARY = "secondary"


class LsbootLocalLunImagePath(ManagedObject):
    """This is LsbootLocalLunImagePath class."""

    consts = LsbootLocalLunImagePathConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("LsbootLocalLunImagePath", "lsbootLocalLunImagePath", "lunimgpath-[type]", VersionMeta.Version224a, "InputOutput", 0x3fL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], [u'lsbootLocalHddImage'], [u'lsbootUEFIBootParam'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "lun_name": MoPropertyMeta("lun_name", "lunName", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version224a, MoPropertyMeta.NAMING, 0x20L, None, None, None, ["primary", "secondary"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lunName": "lun_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.lun_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LsbootLocalLunImagePath", parent_mo_or_dn, **kwargs)

