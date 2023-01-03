#lists in python are represented by []
#We access elements in a list using their indices
#Elements in a list are separated by comma

market_stuff = ['Fish', 'bags', 'tomatoes']
print(market_stuff)

print(market_stuff[0].title())
print(market_stuff[1].title())
print(market_stuff[2].title())

#python has a special syntax for accessing last element in a list
#The use of -1 is use to access the last element in a list
print(market_stuff[-1])

#Exercise
#3-1 Names: : Store the names of a few of your friends in a list called names.
#solution

names = ['Ama', 'Yaw', 'Esther', 'Amponsah']
print(names[-2])

#3-2 Greetings: 
message = "Hello" + " " + names[1].title() + "," + "" + "Congrats!"
print(message)

