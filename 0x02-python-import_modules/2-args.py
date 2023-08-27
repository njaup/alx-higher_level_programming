#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    num_arguments = len(argv)

    if num_arguments == 0:
        print("Number of argument(s): 0\n.")
    elif num_arguments == 1:
        print("Number of argument(s): 1\n1:", argv[0])
    else:
        print(f"Number of argument(s): {num_arguments}\n:")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
