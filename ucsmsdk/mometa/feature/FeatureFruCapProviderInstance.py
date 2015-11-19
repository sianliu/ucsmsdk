"""This module contains the general information for FeatureFruCapProviderInstance ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FeatureFruCapProviderInstanceConsts():
    SUPPORTABILITY_DEPRECATED = "deprecated"
    SUPPORTABILITY_NOT_SUPPORTED = "not-supported"
    SUPPORTABILITY_SUPPORTED = "supported"


class FeatureFruCapProviderInstance(ManagedObject):
    """This is FeatureFruCapProviderInstance class."""

    consts = FeatureFruCapProviderInstanceConsts()
    naming_props = set([u'vendor', u'model', u'revision'])

    mo_meta = MoMeta("FeatureFruCapProviderInstance", "featureFruCapProviderInstance", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version302a, "InputOutput", 0x7fL, [], [""], [u'featureContextEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x4L, 1, 510, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x8L, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supportability": MoPropertyMeta("supportability", "supportability", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deprecated", "not-supported", "supported"], []), 
        "target_dn": MoPropertyMeta("target_dn", "targetDn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x40L, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportability": "supportability", 
        "targetDn": "target_dn", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.sacl = None
        self.status = None
        self.supportability = None
        self.target_dn = None

        ManagedObject.__init__(self, "FeatureFruCapProviderInstance", parent_mo_or_dn, **kwargs)

