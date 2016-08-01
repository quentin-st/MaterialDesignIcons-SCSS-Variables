#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from upstream_parser import mdi_upstream

icon_prefix = 'mdi-'
output_file = 'dist/_materialdesignicons-vars.scss'
output_header = """/**
 * MaterialDesignIcons-SCSS-Variables
 * https://github.com/chteuchteu/MaterialDesignIcons-SCSS-Variables
 *
 * MaterialDesignIcons v#VERSION#
 */\n\n"""

# Download & parse input file
meta = mdi_upstream.fetch_meta()

if len(meta['icons']) == 0:
    print('Could not find variables.')
    sys.exit(1)

# Write in dist file
with open(output_file, 'w') as output:
    output.truncate()

    output.writelines(output_header.replace('#VERSION#', meta['version']))

    for icon in meta['icons']:
        icon_name = icon['name']
        icon_hex = icon['codepoint']

        output.write('${}: "\{}";\n'.format(icon_prefix + icon_name, icon_hex))

    print("Generated {} with {} variables".format(output_file, len(meta['icons'])))
