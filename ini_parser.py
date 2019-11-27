import os
import re
from collections import defaultdict


class INIParser:
    def __init__(self, silent: bool = False, default: str = '__default__'):
        self.silent = silent
        self.default = default
        
    def parse(self, filepath: str) -> dict:
        if not os.path.isfile(filepath):
            raise Exception('File not found') 

        config, slot = defaultdict(dict), self.default
        pattern = re.compile(r'^\[(\w+)\]$')  # section pattern

        with open(filepath, 'r') as fd:
            for line in fd:
                line = line.strip()

                # ignore comments
                if len(line) == 0 or line[0] in {'#', ';'}:
                    continue

                section = pattern.fullmatch(line)
                if section is not None:
                    slot = section.group(1)
                    continue

                # parse key-value pairs
                if '=' in line:
                    pair = line.split('=')

                    # check for valid pair
                    if len(pair) != 2:
                        if self.silent:
                            continue
                        raise Exception('Invalid INI file format')

                    val = pair[1].strip()

                    # cast type to int
                    if val.isnumeric() and not val.startswith('0'):
                        val = int(val)

                    config[slot][pair[0].strip()] = val
                elif not self.silent:
                    raise Exception('Invalid INI file format')

        return dict(config)


if __name__ == '__main__':
    parser = INIParser()
    config = parser.parse('config.ini')
    print(config)
