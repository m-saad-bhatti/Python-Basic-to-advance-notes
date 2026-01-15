tup=(2,1,3,4)
print(type(tup))
print(tup[0])
list=(1) #this is not a tuple, this is a integer
print(list)
print(type(list)) #<class 'int'>
list=(1,) #this is a tuple
print(list)
print(type(list)) #<class 'tuple'>

#slicing in tuple
print(tup[0:2])
#tup.sort() AttributeError: 'tuple' object has no attribute 'sort'

#methods in tuple
tupl=(1,2,3,4,5,2,7,2,9)
print(tupl.index(5))#here index method is used to find the index of the element
print(tupl.count(2))#here count method is used to find the number of times the element is repeated in the tuple