# Sets in Python
"""
A set is an unordered collection of unique elements.
Sets are mutable, which means you can change their elements once they are assigned.
We can not add a lsit or dictionary in a set.
We can add tuple,float,str,int,boolean in a set.
"""
# Creating a set
set1 = {1, 2.3, 3, 4, 5,"Ali",True}
print(set1)
print(type(set1))

# Set ignores duplicate elements
set2 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(set2)

# Set does not support indexing
# print(set1[0]) # TypeError: 'set' object is not subscriptable

#set is unordered
set3= {1, 2.3, 3, 4,"Ali",True,5} #this set will be printed in a random order
print(set3)

# making an empty set
set4 = set()
print(set4)
# we can not make an empty set like this
# set5 = {} # this is a dictionary

#methods in set
set5 = set()
set5.add(10)
set5.add(20)
set5.add(30)    
set5.add(1)
set5.add("Saad")
set5.add(True)
print(set5)
print(len(set5))
set5.remove(1)
print(set5)
set5.clear() #this will remove all the elements from the set
print(set5)

set6 = {1, 2, 3, 4, 5}
print(set6)
set6.pop() #this will remove the first element from the set
print(set6)
set6.pop()
print(set6)

#set union and intersection
set7 = {1, 2, 3, 4, 5} 
set8 = {4, 5, 6, 7, 8}
print(set7.union(set8)) #this will print the union of both sets
print(set7.intersection(set8)) #this will print the intersection of both sets