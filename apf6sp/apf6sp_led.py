#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

from migen import *
from migen.fhdl import *
from migen.build.generic_platform import Pins, IOStandard, Subsignal
from migen.build.platforms import apf6sp
from migen.build.altera.common import AlteraDifferentialInputImpl

ios = [ ("user_led", 0, Pins("HIROSE:D0")),]

plat = apf6sp.Platform()
plat.add_extension(ios)
led = plat.request("user_led", 0)  # led pin on apf6sp_dev

m = Module()
cd_sys = ClockDomain(name="cd_sys", reset_less=True)
m.clock_domains += cd_sys

#class AlteraDifferentialInputImpl(Module):
#    def __init__(self, i_p, i_n, o):
#        self.specials += Instance("ALT_INBUF_DIFF",
#                                  name="ibuf_diff",
#                                  i_i=i_p,
#                                  i_ibar=i_n,
#                                  o_o=o)
#

pcie_clk = plat.request("pcie_clk")
pci_clk_sig = Signal()

m.specials += Instance("altera_pll",
		        i_rst=0,
		        o_outclk=cd_sys.clk,
#		        o_locked="open",
		        i_refclk=pci_clk_sig,

		        p_fractional_vco_multiplier="false",
		        p_reference_clock_frequency="125.0 MHz",
		        p_operation_mode="direct",
		        p_number_of_clocks=1,
		        p_output_clock_frequency0="62.500000 MHz",
		        p_phase_shift0="0 ps",
		        p_duty_cycle0=50,
		        p_output_clock_frequency1="0 MHz",
		        p_phase_shift1="0 ps",
		        p_duty_cycle1=50,
		        p_output_clock_frequency2="0 MHz",
		        p_phase_shift2="0 ps",
		        p_duty_cycle2=50,
		        p_output_clock_frequency3="0 MHz",
		        p_phase_shift3="0 ps",
		        p_duty_cycle3=50,
		        p_output_clock_frequency4="0 MHz",
		        p_phase_shift4="0 ps",
		        p_duty_cycle4=50,
		        p_output_clock_frequency5="0 MHz",
		        p_phase_shift5="0 ps",
		        p_duty_cycle5=50,
		        p_output_clock_frequency6="0 MHz",
		        p_phase_shift6="0 ps",
		        p_duty_cycle6=50,
		        p_output_clock_frequency7="0 MHz",
		        p_phase_shift7="0 ps",
		        p_duty_cycle7=50,
		        p_output_clock_frequency8="0 MHz",
		        p_phase_shift8="0 ps",
		        p_duty_cycle8=50,
		        p_output_clock_frequency9="0 MHz",
		        p_phase_shift9="0 ps",
		        p_duty_cycle9=50,
		        p_output_clock_frequency10="0 MHz",
		        p_phase_shift10="0 ps",
		        p_duty_cycle10=50,
		        p_output_clock_frequency11="0 MHz",
		        p_phase_shift11="0 ps",
		        p_duty_cycle11=50,
		        p_output_clock_frequency12="0 MHz",
		        p_phase_shift12="0 ps",
		        p_duty_cycle12=50,
		        p_output_clock_frequency13="0 MHz",
		        p_phase_shift13="0 ps",
		        p_duty_cycle13=50,
		        p_output_clock_frequency14="0 MHz",
		        p_phase_shift14="0 ps",
		        p_duty_cycle14=50,
		        p_output_clock_frequency15="0 MHz",
		        p_phase_shift15="0 ps",
		        p_duty_cycle15=50,
		        p_output_clock_frequency16="0 MHz",
		        p_phase_shift16="0 ps",
		        p_duty_cycle16=50,
		        p_output_clock_frequency17="0 MHz",
		        p_phase_shift17="0 ps",
		        p_pll_subtype="General",
		        p_pll_type="General",
		        p_duty_cycle17=50
                        ),
m.specials += Instance("ALT_INBUF_DIFF", name="ibuf_diff", i_i=pcie_clk.p, i_ibar=pcie_clk.n, o_o=pci_clk_sig),

counter = Signal(26)
m.comb += led.eq(counter[25])
m.sync += counter.eq(counter + 1)

plat.build(m)
