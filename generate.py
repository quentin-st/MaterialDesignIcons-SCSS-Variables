#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import re

icon_prefix = 'mdi-'
input_file = 'input/_materialdesignicons.scss'
output_file = 'generated/_materialdesignicons-vars.scss'
output_header = """/**
 * MaterialDesignIcons-SCSS-Variables
 * https://github.com/chteuchteu/MaterialDesignIcons-SCSS-Variables
 */\n\n"""

# Check if input file exists
if not os.path.isfile(input_file):
    print("Missing input file")
    sys.exit(1)

# Read & parse input file
input = open(input_file, 'r').readlines()

# First line contains keys, second line contains values
icons_hexes_raw = input[0]
icons_names_raw = input[1]

regex = re.compile("'(.*?)'")
icons_hexes = regex.findall(icons_hexes_raw)
icons_names = regex.findall(icons_names_raw)

if len(icons_hexes) != len(icons_names):
    print("Hexes and names arrays length does not match")
    sys.exit(1)

# Write in generated file
output = open(output_file, 'w')
output.truncate()

output.writelines(output_header)

for i in range(len(icons_hexes)):
    icon_hex = icons_hexes[i]
    icon_name = icons_names[i]

    output.write('${}: "\{}";\n'.format(icon_prefix + icon_name, icon_hex))

print("Generated {} with {} variables".format(output_file, len(icons_hexes)))
