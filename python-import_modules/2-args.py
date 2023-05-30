#!/usr/bin/python3
if __name__ == "__main__":
    def main(argv):
        length = len(argv)
        if length == 1:
            print("0 arguments.")
        elif length == 2:
            print("1 argument:")
            print("{} {}".format(length - 1), argv)
        else:
            for argv in range(length):
                print("{} arguments:".format(length - 1))
                print("{} {}".format(length - 1), argv)
