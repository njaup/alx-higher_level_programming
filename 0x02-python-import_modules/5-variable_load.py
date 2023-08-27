#!/usr/bin/python3
def main():
    module = __import__("variable_load_5")
    a = getattr(module, "a")
    print(a)

if __name__ == "__main__":
    main()
