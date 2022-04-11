# Copyright 2022 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of AttributesTest,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import cadwork
import element_controller as ec
import attribute_controller as ac

elements = cadwork.get_auto_attribute_elements()

for element in elements:
    parent_element = ec.get_parent_container_id(element)
    if parent_element > 0:
        parent_element_production_number = ac.get_production_number(parent_element)
        cadwork.set_auto_attribute([element], str(parent_element_production_number))
