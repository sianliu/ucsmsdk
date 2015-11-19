"""This module contains the general information for ClitestTypeTest2 ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ClitestTypeTest2Consts():
    A_PARTIAL_ENUM_DEFAULT = "default"
    A_PARTIAL_ENUM_UNTAGGED = "untagged"
    FILE_PROTO_FTP = "ftp"
    FILE_PROTO_HTTP = "http"
    FILE_PROTO_NFS_COPY = "nfs-copy"
    FILE_PROTO_NONE = "none"
    FILE_PROTO_SCP = "scp"
    FILE_PROTO_SFTP = "sftp"
    FILE_PROTO_TFTP = "tftp"


class ClitestTypeTest2(ManagedObject):
    """This is ClitestTypeTest2 class."""

    consts = ClitestTypeTest2Consts()
    naming_props = set([])

    mo_meta = MoMeta("ClitestTypeTest2", "clitestTypeTest2", "tt2-", VersionMeta.Version101e, "InputOutput", 0x7fffL, [], ["admin"], [u'topRoot'], [], ["Get"])

    prop_meta = {
        "a_partial_enum": MoPropertyMeta("a_partial_enum", "aPartialEnum", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["default", "untagged"], ["0-4096"]), 
        "abitmask": MoPropertyMeta("abitmask", "abitmask", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """((up|down|kindOfUp|sortOfDown),){0,3}(up|down|kindOfUp|sortOfDown){0,1}""", [], []), 
        "acharbuf": MoPropertyMeta("acharbuf", "acharbuf", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x8L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "file_dir": MoPropertyMeta("file_dir", "fileDir", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], []), 
        "file_host": MoPropertyMeta("file_host", "fileHost", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], []), 
        "file_name": MoPropertyMeta("file_name", "fileName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, 0, 510, None, [], []), 
        "file_passwd": MoPropertyMeta("file_passwd", "filePasswd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,80}""", [], []), 
        "file_path": MoPropertyMeta("file_path", "filePath", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, 0, 510, None, [], []), 
        "file_port": MoPropertyMeta("file_port", "filePort", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], []), 
        "file_proto": MoPropertyMeta("file_proto", "fileProto", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], []), 
        "file_user": MoPropertyMeta("file_user", "fileUser", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2000L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "aPartialEnum": "a_partial_enum", 
        "abitmask": "abitmask", 
        "acharbuf": "acharbuf", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fileDir": "file_dir", 
        "fileHost": "file_host", 
        "fileName": "file_name", 
        "filePasswd": "file_passwd", 
        "filePath": "file_path", 
        "filePort": "file_port", 
        "fileProto": "file_proto", 
        "fileUser": "file_user", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.a_partial_enum = None
        self.abitmask = None
        self.acharbuf = None
        self.child_action = None
        self.file_dir = None
        self.file_host = None
        self.file_name = None
        self.file_passwd = None
        self.file_path = None
        self.file_port = None
        self.file_proto = None
        self.file_user = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ClitestTypeTest2", **kwargs)

