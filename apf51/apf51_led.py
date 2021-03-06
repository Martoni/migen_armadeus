#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

from migen import *
from migen.fhdl import *
from migen.build.generic_platform import Pins, IOStandard
from migen.build.platforms import apf51
 
ios = [
    ("user_led", 0, Pins("J2:15"), IOStandard("LVCMOS33"))
]
 
plat = apf51.Platform()
plat.add_extension(ios)
led = plat.request("user_led", 0)  # led pin on apf51dev
m = Module()
counter = Signal(26)
m.comb += led.eq(counter[25])
m.sync += counter.eq(counter + 1)
plat.build(m)
