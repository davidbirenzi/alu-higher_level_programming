#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name itself
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "" if argc == 1 else "s"))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
