#!/usr/bin/env python3

import sys

argv = sys.argv
argv.pop(0)
argc = len(argv)

print(f"parameters: {argc}")

if argc > 0:
    for arg in argv:
        print(f"{arg}: {len(arg)}")
else:
    print("none")