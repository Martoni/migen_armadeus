#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

from migen import *
from migen.fhdl import *
from migen.build.generic_platform import Pins, IOStandard, Subsignal
from migen.build.platforms import apf6sp

ios = [ ("user_led", 0, Pins("HIROSE:D0")),]

plat = apf6sp.Platform()
plat.add_extension(ios)
led = plat.request("user_led", 0)  # led pin on apf6sp_dev

m = Module()
plat.adding_pll_pcie_clk(m) # need a PLL on main clock
counter = Signal(26)
m.comb += led.eq(counter[25])
m.sync += counter.eq(counter + 1)

plat.build(m)

#XXX generate the rbf, should be integrated in platform build
import os
os.system("quartus_cpf -c build/top.sof top.rbf")
