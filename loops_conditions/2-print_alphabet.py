for i in range(ord('a'), ord('z') + 1):
    print("{:s}".format(chr(i)))

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i))