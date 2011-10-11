#!/usr/bin/env python

def foo(arg1, arg2):
    return int(arg1) + int(arg2)

if __name__ == "__main__":
   import sys
   print foo(sys.argv[1], sys.argv[2])