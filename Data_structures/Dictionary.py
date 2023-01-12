#Dictionaries are used to store data values in key pairs
#Dictionaries are represented with curly braces i.e {}

#  PROPERTIES OF DICTIONARIES
    #Ordered
    #changeable
    #Do not allow duplicates
'''
eg: of a dictionary

my_dict = {
    "Name": "Isaac"
    "Age": 27
    "Occupation": "student"    
}
print(my_dict)
'''
#to tell the length of a dictionary, we use the len() fumction
# i.e len(my_dict)
# Aside curly braces {}, the dict() constructor is also used to make a dictionary
# i.e 
'''
my_dict = dict("Name" = "Isaac", "Age" = 27, "Occupation" = "student")
print(my_dict)
'''
 # ACCESSING ITEMS IN DICTIONARIES
 # One way of accessing items in a dictionary is to use the get() method
 '''example:  x = my_dict.get("Name")'''
             '''print(x)'''
 # To get the keys in a dictionary, we use the key() method
 '''i.e x = my_dict.keys() , this returns the keys in a list[] inside a tuple()'''
 
 # Likewise, the values of the dictionary can also be gotten using the values() method
 # i.e x = my_dict.values(), this returns all the values of the dictionary in a list[] inside a tuple()
 # The items() method returns each item in the dictionary as tuples in a list
 ''' i.e  my_dict.items()'''
 
 #  CHECKING IF KEY EXISTS IN A DICTIONARY
 # To check if a key exists in a dictionary we use th in keyword
 ''' i.e if "Name" in my_dict
      print("Name")
 '''
 # Since one of the properties of python dictionaries is changeability, we can make changes to our dictionary
 # A specific item's value can be changed by referring to its key
 '''i.e my_dict["Age"] = 56 
    or
    Using the update() method
    i.e my_dict.update({"Age": 56}) NB: Take note of the curly braces inside the method
 '''
 #  ADDING ITEMS TO A DICTIONARY
 # Items can be added to a dictionary using a new index key and assigning it to a value
 ''' i.e my_dict["Color"] = "Red" 
            print(my_dict)
    Another approach is to use the update() method, if the item is not in the dictionary, it will be added
    i.e  my_dict.update({"Color: "Red"})
 '''
 