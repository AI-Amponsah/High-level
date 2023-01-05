#floating point numbers are simply decimal numbers

number = float(input("Enter a float: "))
print("The value in 2dp is {:.2f}".format(number))

#simple compound interest code

principal = input("Enter the Principal and Rate: ")
rate = input("Enter the  Rate: ")
principal = float(principal)
rate = float(rate) * .01

for i in range(10):
    principal = principal + (principal * rate)
print("The pricipal after 10 years is {:.2f}".format(principal))
