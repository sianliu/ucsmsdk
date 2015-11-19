"""This module contains the general information for ApeMenlo ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeMenloConsts():
    TYPE_MENLO = "Menlo"
    TYPE_OPLIN = "Oplin"
    TYPE_PALO = "Palo"
    TYPE_UNKNOWN = "Unknown"


class ApeMenlo(ManagedObject):
    """This is ApeMenlo class."""

    consts = ApeMenloConsts()
    naming_props = set([u'mac1'])

    mo_meta = MoMeta("ApeMenlo", "apeMenlo", "Menlo-[mac1]", VersionMeta.Version101e, "InputOutput", 0x3ffffL, [], ["read-only"], [u'apeNicAgManager'], [u'apeMenloVnic', u'apePaloVnic'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "fru_id": MoPropertyMeta("fru_id", "fruId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, 0, 510, None, [], []), 
        "fw_update_timeout": MoPropertyMeta("fw_update_timeout", "fwUpdateTimeout", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "hw_version": MoPropertyMeta("hw_version", "hwVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], []), 
        "mac1": MoPropertyMeta("mac1", "mac1", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "mac2": MoPropertyMeta("mac2", "mac2", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "operation_timeout": MoPropertyMeta("operation_timeout", "operationTimeout", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x400L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "start_event": MoPropertyMeta("start_event", "startEvent", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sw_backup_version": MoPropertyMeta("sw_backup_version", "swBackupVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x2000L, 0, 510, None, [], []), 
        "sw_startup_version": MoPropertyMeta("sw_startup_version", "swStartupVersion", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x4000L, 0, 510, None, [], []), 
        "sw_version": MoPropertyMeta("sw_version", "swVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, 0, 510, None, [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, None, ["Menlo", "Oplin", "Palo", "Unknown"], []), 
        "uplink_port_type": MoPropertyMeta("uplink_port_type", "uplinkPortType", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "fruId": "fru_id", 
        "fwUpdateTimeout": "fw_update_timeout", 
        "hwVersion": "hw_version", 
        "mac1": "mac1", 
        "mac2": "mac2", 
        "name": "name", 
        "operationTimeout": "operation_timeout", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "startEvent": "start_event", 
        "status": "status", 
        "swBackupVersion": "sw_backup_version", 
        "swStartupVersion": "sw_startup_version", 
        "swVersion": "sw_version", 
        "type": "type", 
        "uplinkPortType": "uplink_port_type", 
    }

    def __init__(self, parent_mo_or_dn, mac1, **kwargs):
        self._dirty_mask = 0
        self.mac1 = mac1
        self.child_action = None
        self.description = None
        self.fru_id = None
        self.fw_update_timeout = None
        self.hw_version = None
        self.mac2 = None
        self.name = None
        self.operation_timeout = None
        self.sacl = None
        self.serial = None
        self.start_event = None
        self.status = None
        self.sw_backup_version = None
        self.sw_startup_version = None
        self.sw_version = None
        self.type = None
        self.uplink_port_type = None

        ManagedObject.__init__(self, "ApeMenlo", parent_mo_or_dn, **kwargs)

