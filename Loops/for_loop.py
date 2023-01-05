#for loop is use to make iterations

for i in [1,5,8,7,3]:
    print("i = ", i)

#using range
for i in range(5, 20, 5):
    print("i = ", i)

#printing odds from 0 to 20

for i in range(21):
    if (i % 2) != 0:
        print("{} is odd".format(i))
    else:
         print("{} is even".format(i))
