#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from upstream_parser import mdi_upstream

icon_prefix = 'mdi-'
output_file = 'dist/_materialdesignicons-vars.scss'
output_file_char = 'dist/_materialdesignicons-vars-char.scss'
output_header = """/**
 * MaterialDesignIcons-SCSS-Variables
 * https://github.com/chteuchteu/MaterialDesignIcons-SCSS-Variables
 *
 * MaterialDesignIcons v#VERSION#
 */\n\n"""
output_type_codepoint = 1
output_type_char = 2


def write_to_file(filename, output_type):
    with open(filename, 'w') as output:
        output.truncate()

        output.writelines(output_header.replace('#VERSION#', meta['version']))

        for icon in meta['icons']:
            icon_name = icon['name']
            icon_hex = icon['codepoint']

            if output_type == output_type_codepoint:
                output.write('${}: "\{}";\n'.format(icon_prefix + icon_name, icon_hex))
            elif output_type == output_type_char:
                output.write('${}: char({});\n'.format(icon_prefix + icon_name, icon_hex[0:]))

        print("Generated {} with {} variables".format(filename, len(meta['icons'])))


# Download & parse input file
meta = mdi_upstream.fetch_meta()

if len(meta['icons']) == 0:
    print('Could not find variables.')
    sys.exit(1)

# Write in dist file
write_to_file(output_file, output_type_codepoint)
write_to_file(output_file_char, output_type_char)
