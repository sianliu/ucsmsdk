"""This module contains the general information for BiosVfQPILinkFrequencySelect ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfQPILinkFrequencySelectConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_QPILINK_FREQUENCY_SELECT_6400 = "6400"
    VP_QPILINK_FREQUENCY_SELECT_7200 = "7200"
    VP_QPILINK_FREQUENCY_SELECT_8000 = "8000"
    VP_QPILINK_FREQUENCY_SELECT_9600 = "9600"
    VP_QPILINK_FREQUENCY_SELECT_AUTO = "auto"
    VP_QPILINK_FREQUENCY_SELECT_PLATFORM_DEFAULT = "platform-default"
    VP_QPILINK_FREQUENCY_SELECT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfQPILinkFrequencySelect(ManagedObject):
    """This is BiosVfQPILinkFrequencySelect class."""

    consts = BiosVfQPILinkFrequencySelectConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfQPILinkFrequencySelect", "biosVfQPILinkFrequencySelect", "QPI-Link-Frequency-Select", VersionMeta.Version222c, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_qpi_link_frequency_select": MoPropertyMeta("vp_qpi_link_frequency_select", "vpQPILinkFrequencySelect", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["6400", "7200", "8000", "9600", "auto", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpQPILinkFrequencySelect": "vp_qpi_link_frequency_select", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_qpi_link_frequency_select = None

        ManagedObject.__init__(self, "BiosVfQPILinkFrequencySelect", parent_mo_or_dn, **kwargs)

