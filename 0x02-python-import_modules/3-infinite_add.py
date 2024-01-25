#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    tally = 0
    for count in range(len(sys.argv) - 1):
        tally += int(sys.argv[count + 1])
    print("{}".format(tally))
