"""This module contains the general information for SwNetflowMonitorRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SwNetflowMonitorRefConsts():
    DIRECTION_RECEIVE = "receive"
    DIRECTION_TRANSMIT = "transmit"
    KEY_TYPE_IPV4KEYS = "ipv4keys"
    KEY_TYPE_IPV6KEYS = "ipv6keys"
    KEY_TYPE_L2KEYS = "l2keys"


class SwNetflowMonitorRef(ManagedObject):
    """This is SwNetflowMonitorRef class."""

    consts = SwNetflowMonitorRefConsts()
    naming_props = set([u'name', u'direction'])

    mo_meta = MoMeta("SwNetflowMonitorRef", "swNetflowMonitorRef", "nf-monitor-ref-[name]-[direction]", VersionMeta.Version221b, "InputOutput", 0x3fL, [], ["read-only"], [u'dcxVc', u'swNetflowMonSession', u'vnicProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "direction": MoPropertyMeta("direction", "direction", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x2L, None, None, None, ["receive", "transmit"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "key_type": MoPropertyMeta("key_type", "keyType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4keys", "ipv6keys", "l2keys"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "source_dn": MoPropertyMeta("source_dn", "sourceDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "direction": "direction", 
        "dn": "dn", 
        "keyType": "key_type", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceDn": "source_dn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, direction, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.direction = direction
        self.child_action = None
        self.key_type = None
        self.sacl = None
        self.source_dn = None
        self.status = None

        ManagedObject.__init__(self, "SwNetflowMonitorRef", parent_mo_or_dn, **kwargs)

