#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("0 arguments")
    else:
        count = 0
        args = len(sys.argv) - 1
        print("{} argument{}:".format(args, "s" if args != 1 else ""))
        for i in sys.argv:
            if count == 0:
                count += 1
                continue
            print("{}: {}".format(count, i))
            count += 1
