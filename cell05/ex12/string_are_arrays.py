#!/usr/bin/env python3

import sys

argv = sys.argv
argc = len(argv) - 1

# print(argv[1].count("z"))
countz = argv[1].count("z")
if argc == 1 and countz > 0:
    print("z" * countz)
else:
    print("none")