#!/usr/bin/python3
import sys
def main():
    arguments = sys.argv[1:]

    if not arguments:
        print("0")
        return

    total_sum = 0
    for arg in arguments:
        total_sum += int(arg)

    print(total_sum)

if __name__ == "__main__":
    main()
