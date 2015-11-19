"""This module contains the general information for BiosVfPCISlotLinkSpeed ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfPCISlotLinkSpeedConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PCIE_SLOT10_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT10_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT10_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT10_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT10_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT10_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT10_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT1_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT1_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT1_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT1_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT1_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT1_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT2_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT2_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT2_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT2_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT2_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT2_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT3_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT3_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT3_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT3_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT3_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT3_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT3_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT4_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT4_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT4_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT4_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT4_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT4_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT4_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT5_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT5_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT5_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT5_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT5_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT5_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT5_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT6_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT6_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT6_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT6_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT6_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT6_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT6_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT7_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT7_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT7_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT7_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT7_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT7_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT7_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT8_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT8_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT8_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT8_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT8_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT8_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT8_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT9_LINK_SPEED_AUTO = "auto"
    VP_PCIE_SLOT9_LINK_SPEED_DISABLED = "disabled"
    VP_PCIE_SLOT9_LINK_SPEED_GEN1 = "gen1"
    VP_PCIE_SLOT9_LINK_SPEED_GEN2 = "gen2"
    VP_PCIE_SLOT9_LINK_SPEED_GEN3 = "gen3"
    VP_PCIE_SLOT9_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT9_LINK_SPEED_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfPCISlotLinkSpeed(ManagedObject):
    """This is BiosVfPCISlotLinkSpeed class."""

    consts = BiosVfPCISlotLinkSpeedConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfPCISlotLinkSpeed", "biosVfPCISlotLinkSpeed", "PCI-Slot-Link-Speed", VersionMeta.Version222c, "InputOutput", 0x3fffL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_pc_ie_slot10_link_speed": MoPropertyMeta("vp_pc_ie_slot10_link_speed", "vpPCIeSlot10LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot1_link_speed": MoPropertyMeta("vp_pc_ie_slot1_link_speed", "vpPCIeSlot1LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot2_link_speed": MoPropertyMeta("vp_pc_ie_slot2_link_speed", "vpPCIeSlot2LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot3_link_speed": MoPropertyMeta("vp_pc_ie_slot3_link_speed", "vpPCIeSlot3LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot4_link_speed": MoPropertyMeta("vp_pc_ie_slot4_link_speed", "vpPCIeSlot4LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot5_link_speed": MoPropertyMeta("vp_pc_ie_slot5_link_speed", "vpPCIeSlot5LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot6_link_speed": MoPropertyMeta("vp_pc_ie_slot6_link_speed", "vpPCIeSlot6LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot7_link_speed": MoPropertyMeta("vp_pc_ie_slot7_link_speed", "vpPCIeSlot7LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot8_link_speed": MoPropertyMeta("vp_pc_ie_slot8_link_speed", "vpPCIeSlot8LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
        "vp_pc_ie_slot9_link_speed": MoPropertyMeta("vp_pc_ie_slot9_link_speed", "vpPCIeSlot9LinkSpeed", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["auto", "disabled", "gen1", "gen2", "gen3", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpPCIeSlot10LinkSpeed": "vp_pc_ie_slot10_link_speed", 
        "vpPCIeSlot1LinkSpeed": "vp_pc_ie_slot1_link_speed", 
        "vpPCIeSlot2LinkSpeed": "vp_pc_ie_slot2_link_speed", 
        "vpPCIeSlot3LinkSpeed": "vp_pc_ie_slot3_link_speed", 
        "vpPCIeSlot4LinkSpeed": "vp_pc_ie_slot4_link_speed", 
        "vpPCIeSlot5LinkSpeed": "vp_pc_ie_slot5_link_speed", 
        "vpPCIeSlot6LinkSpeed": "vp_pc_ie_slot6_link_speed", 
        "vpPCIeSlot7LinkSpeed": "vp_pc_ie_slot7_link_speed", 
        "vpPCIeSlot8LinkSpeed": "vp_pc_ie_slot8_link_speed", 
        "vpPCIeSlot9LinkSpeed": "vp_pc_ie_slot9_link_speed", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_pc_ie_slot10_link_speed = None
        self.vp_pc_ie_slot1_link_speed = None
        self.vp_pc_ie_slot2_link_speed = None
        self.vp_pc_ie_slot3_link_speed = None
        self.vp_pc_ie_slot4_link_speed = None
        self.vp_pc_ie_slot5_link_speed = None
        self.vp_pc_ie_slot6_link_speed = None
        self.vp_pc_ie_slot7_link_speed = None
        self.vp_pc_ie_slot8_link_speed = None
        self.vp_pc_ie_slot9_link_speed = None

        ManagedObject.__init__(self, "BiosVfPCISlotLinkSpeed", parent_mo_or_dn, **kwargs)

