
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positve".format(number))
elif number < 0:
     print("{} is negative".format(number))
else:
     print("{} is zero".format(number))