# a= {1:2, 2:3,3:4} # will return type dict
# print (a)
# print (type(a)) # this is dictionary
# b={1,2,3,6,1,2,3,4,5,7,4,5,15,14,13,12} # will return type set
# print (b) # will print non repetitive numbers in ascending order
# print (type (b)) # will return type as set

# # important : empty sets return type as dictionary and not an empty set
# c= {} 
# print (type(c)) 

# d= set() # returns an empty set
# print (type (d))  
# e=list() # returns an empty list
# print (type (e))
# f= tuple() # returns an empty tuple
# print (type(f)) 
# g= dict()  # returns an empty dictionary
# print (type(g)) 
# g.update({1:2})
# print (g)
# g.update({1:3, 3:4, 4:5})
# print (g)


# d.add(1) # number can be added to a set
# d.add(2)
# d.add('sid') # string can be added to a set
# d.add((1,2,3)) # a tuple can be added to a set
# # d.add([1,2,3]) # xxx list cannot be added to a set
# # d.add ({1:3}) # xxx dictionary cannot be added to a set
# print (d)

# sets accepts numbers and displays them randomly in any order
# they are non repeateble and once created cannot be changed 
# sets cannot be called using index number as the order dosent matter 
e={4,5}
print (e)
e.add(3)
e.add(2)
e.add(1)

print (e)
e.add('sid')
e.add('programmer')
print (e)
e.pop()
print (len(e))
e.pop()
print (len(e))
e.pop()
print (len(e))
print (e)



# print (len(e)) # displays the length of items
# e.remove(5) # removes the item 
# e.remove(4)
# e.remove('sid')
# print (e)
 
# print (e.pop())
# print (e)
# print (e.pop())
# print (e)
# print (e.pop())
# print (e)
# print (e.pop())

