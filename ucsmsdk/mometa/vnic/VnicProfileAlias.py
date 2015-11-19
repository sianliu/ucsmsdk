"""This module contains the general information for VnicProfileAlias ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicProfileAliasConsts():
    pass


class VnicProfileAlias(ManagedObject):
    """This is VnicProfileAlias class."""

    consts = VnicProfileAliasConsts()
    naming_props = set([u'swUuid', u'alias'])

    mo_meta = MoMeta("VnicProfileAlias", "vnicProfileAlias", "uuid-[sw_uuid]alias-[alias]", VersionMeta.Version101e, "InputOutput", 0x3fL, [], ["read-only"], [u'vmVnicProfInst', u'vnicProfile'], [], ["Get"])

    prop_meta = {
        "alias": MoPropertyMeta("alias", "alias", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x1L, 1, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sw_uuid": MoPropertyMeta("sw_uuid", "swUuid", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x20L, None, None, """(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
    }

    prop_map = {
        "alias": "alias", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "swUuid": "sw_uuid", 
    }

    def __init__(self, parent_mo_or_dn, sw_uuid, alias, **kwargs):
        self._dirty_mask = 0
        self.sw_uuid = sw_uuid
        self.alias = alias
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicProfileAlias", parent_mo_or_dn, **kwargs)

