# dictionary = one of the 4 collection types in python
# dictionary = a collection of {key:value} pair
# ordered and changeable , no duplicates

capitals = {"USA":"Washington DC","India":"New Delhi","China":"Beijing","Nepal":"Kathmandu"}

#Attributes and methods of a dictionary
#print(dir(capitals))

# Decription of sttributes and methods of a dictionary
#print(help(capitals))

#To get value from a dictionary
#print(capitals.get("India"))

#In case of no such key in the dictionary
#print(capitals.get("Japan"))

#if capitals.get("India"):
#    print("Thats a valid capital")
#else:
#    print("No such capital exists")

#To update the dictionary (add a new {key:value} pair)
#capitals.update({"Antarctica":"Shangrila"})
#print(capitals)

#To update the dictionary (update a new value to {key:value} pair)
#capitals.update({"India":"Ayodhya"})
#print(capitals)

#To remove a key from the dictionary 
#Can only remove by entering key not the value to it
#capitals.pop("New Delhi")
#print(capitals)

# To remove latest item fromt the dictionary
#capitals.popitem()
#print(capitals)

#To remove the key value pairs from entire dictionary
#capitals.clear()
#print(capitals)

#To get Keys from the dictionary
#Will return an object which resembles a list
#a=capitals.keys()
#print(a)

#for a in capitals.keys():
#    print(a)

#To get Values from the dictionary
#Will return an object which resembles a list
#a=capitals.values()
#print(a)

#for a in capitals.values():
#    print(a)

# Items method to get dictionary object which resembles a 2d list of tuples
#items = capitals.items()
#print(items)

for key,value in capitals.items():
    print(f"{key}:{value}")