# Extracted from https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse
# python3 test.py -l "abc xyz, 123"

import re
import argparse

parser = argparse.ArgumentParser(description='Process a list.')
parser.add_argument('-l', '--list',
                    type=lambda s: re.split(' |, ', s),
                    required=True,
                    help='comma or space delimited list of characters')

args = parser.parse_args()
print(args.list)


# Output: ['abc', 'xyz', '123']

