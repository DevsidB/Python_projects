a={"sid": "lalbaug",
'harry':'youtuber', 
'numbers': [1,2,3,4,5,6], 
'harrydict':{'harry':'coder'},
'fruitdict':("orange", "banana", "apple"),
1:2}

# print (type(a.keys())) # prints the type of keys
# print (type(a.values())) # prints the type of values
# print (type(a)) #prints the type of  dictionary
# print (a) # prints the disctionary
# print (list(a)) # prints dictionary to list
# print (tuple(a)) # prints dictionary to tuple
# print (list (a.keys())) #prints keys contained in dictionary as a list
# print (list(a.values())) # prints values contained in a dictionary to list
# print (type(list (a.keys()))) # converts key to list and prints the type
# print (type(list(a.values()))) # converts values to list and prints the type
# print (type(tuple (a.keys()))) # converts keys to tuple and prints the type
# print (type(tuple(a.values()))) # converts values to tuple and prints the type
# print (a.items()) # prints the dictionary in the form of comma separated tuples to be used for loops(key,values)
# print ("haa \n meri \n jaan")
# print ('''haa
# meri 
# jaan''')
# print (a)
a.update({'python':'programming language',
 'book':'reading', 
'harry': 'teacher'}) # '''updates the dictionary with 
                    # new terms. also to note that 'harry': 'teacher' is not created and also not updated in the secondary dict'''
# important interview question - why to use a get command (line 2) when we can do it using (line 1)               
print (a)
# print (a['harry']) #line 1---------------getiing value for harry normal
# print (a.get('harry')) # line 2------------getting value for harry using get command

# print (a.get('harry2'))   # xxx returns none and doesnt throw an error if not present in dict
# print (a['harry2'])   # throws an error if not present in dict

# print (type(a.items()))
print (a.items()) ## prints the dictionary in the form of comma separated tuples to be used for loops(key,values)






