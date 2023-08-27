#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
        print("1:", argv[0])
    else:
        print(f"{num_arguments} arguments:")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
