#!/usr/bin/env python3

a = float(input("Give me a number: "))

rounded = int(a)
if a > rounded:
    rounded += 1

print(rounded)