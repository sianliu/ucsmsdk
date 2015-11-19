"""This module contains the general information for AaaUser ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AaaUserConsts():
    ACCOUNT_STATUS_ACTIVE = "active"
    ACCOUNT_STATUS_INACTIVE = "inactive"
    CLEAR_PWD_HISTORY_NO = "no"
    CLEAR_PWD_HISTORY_YES = "yes"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    ENC_PWD_SET_FALSE = "false"
    ENC_PWD_SET_NO = "no"
    ENC_PWD_SET_TRUE = "true"
    ENC_PWD_SET_YES = "yes"
    EXPIRATION_NEVER = "never"
    EXPIRES_FALSE = "false"
    EXPIRES_NO = "no"
    EXPIRES_TRUE = "true"
    EXPIRES_YES = "yes"
    PWD_LIFE_TIME_NO_PASSWORD_EXPIRE = "no-password-expire"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"


class AaaUser(ManagedObject):
    """This is AaaUser class."""

    consts = AaaUserConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AaaUser", "aaaUser", "user-[name]", VersionMeta.Version101e, "InputOutput", 0x3ffffL, [], ["aaa", "admin"], [u'aaaUserEp'], [u'aaaCimcSession', u'aaaSession', u'aaaSshAuth', u'aaaUserData', u'aaaUserLocale', u'aaaUserRole', u'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "account_status": MoPropertyMeta("account_status", "accountStatus", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["active", "inactive"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clear_pwd_history": MoPropertyMeta("clear_pwd_history", "clearPwdHistory", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["no", "yes"], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []), 
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], []), 
        "enc_pwd": MoPropertyMeta("enc_pwd", "encPwd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, 0, 256, None, [], []), 
        "enc_pwd_set": MoPropertyMeta("enc_pwd_set", "encPwdSet", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["false", "no", "true", "yes"], []), 
        "expiration": MoPropertyMeta("expiration", "expiration", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "expires": MoPropertyMeta("expires", "expires", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["false", "no", "true", "yes"], []), 
        "first_name": MoPropertyMeta("first_name", "firstName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, 0, 32, None, [], []), 
        "last_name": MoPropertyMeta("last_name", "lastName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, 0, 32, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x1000L, None, None, """[a-zA-Z][a-zA-Z0-9_.-]{0,31}""", [], []), 
        "phone": MoPropertyMeta("phone", "phone", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, 0, 510, None, [], []), 
        "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """((ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault),){0,37}(ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault){0,1}""", [], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,80}""", [], []), 
        "pwd_life_time": MoPropertyMeta("pwd_life_time", "pwdLifeTime", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, ["no-password-expire"], ["0-3650"]), 
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10000L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "accountStatus": "account_status", 
        "childAction": "child_action", 
        "clearPwdHistory": "clear_pwd_history", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "descr": "descr", 
        "dn": "dn", 
        "email": "email", 
        "encPwd": "enc_pwd", 
        "encPwdSet": "enc_pwd_set", 
        "expiration": "expiration", 
        "expires": "expires", 
        "firstName": "first_name", 
        "lastName": "last_name", 
        "name": "name", 
        "phone": "phone", 
        "priv": "priv", 
        "pwd": "pwd", 
        "pwdLifeTime": "pwd_life_time", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.account_status = None
        self.child_action = None
        self.clear_pwd_history = None
        self.config_state = None
        self.config_status_message = None
        self.descr = None
        self.email = None
        self.enc_pwd = None
        self.enc_pwd_set = None
        self.expiration = None
        self.expires = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.priv = None
        self.pwd = None
        self.pwd_life_time = None
        self.pwd_set = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AaaUser", parent_mo_or_dn, **kwargs)

