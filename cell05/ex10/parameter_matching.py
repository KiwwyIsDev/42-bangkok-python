#!/usr/bin/env python3

import sys

argv = sys.argv
argc = len(argv) - 1

if argc != 1:
    print("none")
else:
    if input("What was the parameter? ") == argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")