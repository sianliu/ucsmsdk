"""This module contains the meta information of ApeSetAdaptorFirmwareVersion ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeSetAdaptorFirmwareVersion", "apeSetAdaptorFirmwareVersion", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_adaptor_fw_version": MethodPropertyMeta("InAdaptorFwVersion", "inAdaptorFwVersion", "Xs:string", "Version142b", "Input", False),
    "in_adaptor_serial": MethodPropertyMeta("InAdaptorSerial", "inAdaptorSerial", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inAdaptorFwVersion": "in_adaptor_fw_version",
    "inAdaptorSerial": "in_adaptor_serial",
}

