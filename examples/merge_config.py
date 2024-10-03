#!/usr/bin/env python3

# This script functions similarly to scripts/kconfig/merge_config.sh from the
# kernel tree, merging multiple configurations fragments to produce a complete
# .config, with unspecified values filled in as for alldefconfig.
#
# The generated .config respects symbol dependencies, and a warning is printed
# if any symbol gets a different value from the assigned value.
#
# For a real-world merging example based on this script, see
# https://github.com/zephyrproject-rtos/zephyr/blob/master/scripts/kconfig/kconfig.py.
#
# Here's a demo:
#
# Kconfig contents:
#
#     config FOO
#         bool "FOO"
#
#     config BAR
#         bool "BAR"
#
#     config BAZ
#         string "BAZ"
#
#     config QAZ
#         bool "QAZ" if n
#
#
# conf1 contents:
#
#     CONFIG_FOO=y
#
#
# conf2 contents:
#
#     CONFIG_BAR=y
#
#
# conf3 contents:
#
#     # Assigned twice (would generate warning if 'warn_assign_override' was
#     # True)
#     # CONFIG_FOO is not set
#
#     # Ops... this symbol doesn't exist
#     CONFIG_OPS=y
#
#     CONFIG_BAZ="baz string"
#
#
# conf4 contents:
#
#     CONFIG_QAZ=y
#
#
# Running:
#
#     $ python(3) merge_config.py Kconfig merged conf1 conf2 conf3 conf4
#     Merged configuration 'conf1'
#     Merged configuration 'conf2'
#     conf3:5: warning: attempt to assign the value 'y' to the undefined symbol OPS
#     Merged configuration 'conf3'
#     Merged configuration 'conf4'
#     Configuration saved to 'merged'
#     warning: QAZ (defined at Kconfig:10) was assigned the value 'y' but got the value 'n' -- check dependencies
#     $ cat merged
#     Generated by Kconfiglib (https://github.com/zephyrproject-rtos/Kconfiglib)
#     # CONFIG_FOO is not set
#     CONFIG_BAR=y
#     CONFIG_BAZ="baz string"

from __future__ import print_function
import sys

from kconfiglib import Kconfig, BOOL, TRISTATE, TRI_TO_STR


if len(sys.argv) < 4:
    sys.exit("usage: merge_config.py Kconfig merged_config config1 [config2 ...]")

kconf = Kconfig(sys.argv[1], suppress_traceback=True)

# Enable warnings for assignments to undefined symbols
kconf.warn_assign_undef = True

# (This script uses alldefconfig as the base. Other starting states could be
# set up here as well. The approach in examples/allnoconfig_simpler.py could
# provide an allnoconfig starting state for example.)

# Disable warnings generated for multiple assignments to the same symbol within
# a (set of) configuration files. Assigning a symbol multiple times might be
# done intentionally when merging configuration files.
kconf.warn_assign_override = False
kconf.warn_assign_redun = False

# Create a merged configuration by loading the fragments with replace=False.
# load_config() and write_config() returns a message to print.
for config in sys.argv[3:]:
    print(kconf.load_config(config, replace=False))

# Write the merged configuration
print(kconf.write_config(sys.argv[2]))

# Print warnings for symbols whose actual value doesn't match the assigned
# value
for sym in kconf.defined_syms:
    # Was the symbol assigned to?
    if sym.user_value is not None:
        # Tristate values are represented as 0, 1, 2. Having them as
        # "n", "m", "y" is more convenient here, so convert.
        if sym.type in (BOOL, TRISTATE):
            user_value = TRI_TO_STR[sym.user_value]
        else:
            user_value = sym.user_value

        if user_value != sym.str_value:
            print("warning: {} was assigned the value '{}' but got the "
                  "value '{}' -- check dependencies".format(
                      sym.name_and_loc, user_value, sym.str_value),
                  file=sys.stderr)
