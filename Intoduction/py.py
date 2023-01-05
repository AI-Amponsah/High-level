#Converting miles to kg
#Ask user for miles input
miles = int(input("Enter distance:" ))
kg = miles *  1.60934
print("{} miles equals {} kilometers".format(miles, kg))

#Program to determine the grade of a person based on their age

#Ask for the persons age

age = eval(input("Enter your age: " ))

if age == 5:
    print("Kindergarten")
elif (age>= 6) and (age<= 17):
    print("From grades 1 to 12.")
elif age > 17:
    print("College")
else:
    print("Input the correct age range")