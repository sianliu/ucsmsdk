"""This module contains the general information for LsmaintMaintPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LsmaintMaintPolicyConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    UPTIME_DISR_IMMEDIATE = "immediate"
    UPTIME_DISR_TIMER_AUTOMATIC = "timer-automatic"
    UPTIME_DISR_USER_ACK = "user-ack"


class LsmaintMaintPolicy(ManagedObject):
    """This is LsmaintMaintPolicy class."""

    consts = LsmaintMaintPolicyConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LsmaintMaintPolicy", "lsmaintMaintPolicy", "maint-[name]", VersionMeta.Version141i, "InputOutput", 0x1ffL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy"], [u'orgOrg'], [u'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_sched_name": MoPropertyMeta("oper_sched_name", "operSchedName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sched_name": MoPropertyMeta("sched_name", "schedName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uptime_disr": MoPropertyMeta("uptime_disr", "uptimeDisr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["immediate", "timer-automatic", "user-ack"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operSchedName": "oper_sched_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "schedName": "sched_name", 
        "status": "status", 
        "uptimeDisr": "uptime_disr", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.oper_sched_name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.sched_name = None
        self.status = None
        self.uptime_disr = None

        ManagedObject.__init__(self, "LsmaintMaintPolicy", parent_mo_or_dn, **kwargs)

