"""This module contains the meta information of ApeMcGetParam ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeMcGetParam", "apeMcGetParam", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_mc_address": MethodPropertyMeta("InMcAddress", "inMcAddress", "AddressIPv4", "Version142b", "Input", False),
    "in_param": MethodPropertyMeta("InParam", "inParam", "Xs:unsignedInt", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inMcAddress": "in_mc_address",
    "inParam": "in_param",
    "outConfigs": "out_configs",
}

