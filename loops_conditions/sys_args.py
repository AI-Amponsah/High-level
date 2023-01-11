def print_argv(argv):
    num = len(argv) - 1
    if num == 0:
        print("{:d} argument.".format(num))
    else:
        if num == 1:
            print("{:d} argument.".format(num))
        else:
            print("{:d} arguments.".format(num))
        i = 1
        
        while i <= num:
            print("{:d}: {:s} argument.".format(i, argv[i]))

if __name__ == "__main__":
    import sys
    print_argv(sys.argv)