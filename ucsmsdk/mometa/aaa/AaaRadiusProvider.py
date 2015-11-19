"""This module contains the general information for AaaRadiusProvider ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AaaRadiusProviderConsts():
    KEY_SET_FALSE = "false"
    KEY_SET_NO = "no"
    KEY_SET_TRUE = "true"
    KEY_SET_YES = "yes"
    ORDER_LOWEST_AVAILABLE = "lowest-available"
    SERVICE_ACCOUNTING = "accounting"
    SERVICE_ALL = "all"
    SERVICE_AUTHORIZATION = "authorization"


class AaaRadiusProvider(ManagedObject):
    """This is AaaRadiusProvider class."""

    consts = AaaRadiusProviderConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AaaRadiusProvider", "aaaRadiusProvider", "provider-[name]", VersionMeta.Version101e, "InputOutput", 0xfffL, [], ["aaa", "admin"], [u'aaaRadiusEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "auth_port": MoPropertyMeta("auth_port", "authPort", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["1-65535"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "enc_key": MoPropertyMeta("enc_key", "encKey", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, 1, 63, None, [], []), 
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """[!""#$%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,63}""", [], []), 
        "key_set": MoPropertyMeta("key_set", "keySet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40L, None, None, """^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["lowest-available"], ["0-16"]), 
        "retries": MoPropertyMeta("retries", "retries", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, [], ["0-5"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "service": MoPropertyMeta("service", "service", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accounting", "all", "authorization"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], ["0-60"]), 
    }

    prop_map = {
        "authPort": "auth_port", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "encKey": "enc_key", 
        "key": "key", 
        "keySet": "key_set", 
        "name": "name", 
        "order": "order", 
        "retries": "retries", 
        "rn": "rn", 
        "sacl": "sacl", 
        "service": "service", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.auth_port = None
        self.child_action = None
        self.descr = None
        self.enc_key = None
        self.key = None
        self.key_set = None
        self.order = None
        self.retries = None
        self.sacl = None
        self.service = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AaaRadiusProvider", parent_mo_or_dn, **kwargs)

