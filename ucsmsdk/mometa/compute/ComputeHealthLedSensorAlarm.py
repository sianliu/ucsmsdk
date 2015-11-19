"""This module contains the general information for ComputeHealthLedSensorAlarm ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeHealthLedSensorAlarmConsts():
    ALARM_SEVERITY_MINOR = "minor"
    ALARM_SEVERITY_SEVERE = "severe"


class ComputeHealthLedSensorAlarm(ManagedObject):
    """This is ComputeHealthLedSensorAlarm class."""

    consts = ComputeHealthLedSensorAlarmConsts()
    naming_props = set([u'sensorId'])

    mo_meta = MoMeta("ComputeHealthLedSensorAlarm", "computeHealthLedSensorAlarm", "sensor-alarm-[sensor_id]", VersionMeta.Version212a, "InputOutput", 0x1fL, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'equipmentHealthLed'], [], ["Get"])

    prop_meta = {
        "alarm_desc": MoPropertyMeta("alarm_desc", "alarmDesc", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "alarm_severity": MoPropertyMeta("alarm_severity", "alarmSeverity", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["minor", "severe"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sensor_id": MoPropertyMeta("sensor_id", "sensorId", "ushort", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], []), 
        "sensor_name": MoPropertyMeta("sensor_name", "sensorName", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "alarmDesc": "alarm_desc", 
        "alarmSeverity": "alarm_severity", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sensorId": "sensor_id", 
        "sensorName": "sensor_name", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, sensor_id, **kwargs):
        self._dirty_mask = 0
        self.sensor_id = sensor_id
        self.alarm_desc = None
        self.alarm_severity = None
        self.child_action = None
        self.sacl = None
        self.sensor_name = None
        self.status = None

        ManagedObject.__init__(self, "ComputeHealthLedSensorAlarm", parent_mo_or_dn, **kwargs)

