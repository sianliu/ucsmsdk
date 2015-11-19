"""This module contains the general information for CallhomePeriodicSystemInventory ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CallhomePeriodicSystemInventoryConsts():
    ADMIN_STATE_OFF = "off"
    ADMIN_STATE_ON = "on"
    NEXT_DEADLINE_NEVER = "never"
    SEND_NOW_FALSE = "false"
    SEND_NOW_NO = "no"
    SEND_NOW_TRUE = "true"
    SEND_NOW_YES = "yes"
    TIME_OF_LAST_SUCCESS_NEVER = "never"


class CallhomePeriodicSystemInventory(ManagedObject):
    """This is CallhomePeriodicSystemInventory class."""

    consts = CallhomePeriodicSystemInventoryConsts()
    naming_props = set([])

    mo_meta = MoMeta("CallhomePeriodicSystemInventory", "callhomePeriodicSystemInventory", "periodicsysteminventory", VersionMeta.Version101e, "InputOutput", 0x1fffL, [], ["admin", "operations"], [u'callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["off", "on"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "interval_days": MoPropertyMeta("interval_days", "intervalDays", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["1-30"]), 
        "last_deadline": MoPropertyMeta("last_deadline", "lastDeadline", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "maximum_retry_count": MoPropertyMeta("maximum_retry_count", "maximumRetryCount", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["0-5"]), 
        "minimum_send_now_interval_seconds": MoPropertyMeta("minimum_send_now_interval_seconds", "minimumSendNowIntervalSeconds", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["1-2000000000"]), 
        "next_deadline": MoPropertyMeta("next_deadline", "nextDeadline", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "poll_interval_seconds": MoPropertyMeta("poll_interval_seconds", "pollIntervalSeconds", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["10-3600"]), 
        "retry_count": MoPropertyMeta("retry_count", "retryCount", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry_delay_minutes": MoPropertyMeta("retry_delay_minutes", "retryDelayMinutes", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], ["0-60"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "send_now": MoPropertyMeta("send_now", "sendNow", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_of_day_hour": MoPropertyMeta("time_of_day_hour", "timeOfDayHour", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], ["0-23"]), 
        "time_of_day_minute": MoPropertyMeta("time_of_day_minute", "timeOfDayMinute", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, [], ["0-59"]), 
        "time_of_last_attempt": MoPropertyMeta("time_of_last_attempt", "timeOfLastAttempt", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "time_of_last_success": MoPropertyMeta("time_of_last_success", "timeOfLastSuccess", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervalDays": "interval_days", 
        "lastDeadline": "last_deadline", 
        "maximumRetryCount": "maximum_retry_count", 
        "minimumSendNowIntervalSeconds": "minimum_send_now_interval_seconds", 
        "nextDeadline": "next_deadline", 
        "pollIntervalSeconds": "poll_interval_seconds", 
        "retryCount": "retry_count", 
        "retryDelayMinutes": "retry_delay_minutes", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sendNow": "send_now", 
        "status": "status", 
        "timeOfDayHour": "time_of_day_hour", 
        "timeOfDayMinute": "time_of_day_minute", 
        "timeOfLastAttempt": "time_of_last_attempt", 
        "timeOfLastSuccess": "time_of_last_success", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.interval_days = None
        self.last_deadline = None
        self.maximum_retry_count = None
        self.minimum_send_now_interval_seconds = None
        self.next_deadline = None
        self.poll_interval_seconds = None
        self.retry_count = None
        self.retry_delay_minutes = None
        self.sacl = None
        self.send_now = None
        self.status = None
        self.time_of_day_hour = None
        self.time_of_day_minute = None
        self.time_of_last_attempt = None
        self.time_of_last_success = None

        ManagedObject.__init__(self, "CallhomePeriodicSystemInventory", parent_mo_or_dn, **kwargs)

