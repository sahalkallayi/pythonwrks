
#set

name={"hari","sahal","hello","chennai","kollam"}

#print(name)

# duplicates allowed

#elements are unorder

#it doesnt have index position

#mutable

#name.add("kochi")

#print(name)

#name.clear()

#print(name)

#name.pop()

#print(name)

#name.discard("hello")

#print(name)

#name.update() #add elements from any collection to the set

new_names=["hp","lenovo","asus","hello","chennai"]

#name.update(new_names)

#print(name)

#new_set=name.union(new_names) # return the compined elements from two sets and return as a new code

#print(new_set)

#new_set=name.intersection(new_names)

#print(new_set)

#name.difference()

#new_set=name.difference(new_names)

#print(new_set)

new_set=name.symmetric_difference(new_names) #compine all elements from two set and remove common elements

print(new_set)

