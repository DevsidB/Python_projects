mydict= {'pankha': 'fan', 'ghadi': 'clock', 'aaina': 'mirror'}
print ("The options available are:", mydict.keys())
a= input ("Plase enter the hindi word: \n")
# print ("The meaning of the word you entered is : ", mydict[a]) # will throw an eror if word not found
print ("The meaning of the word you entered is : ", mydict.get(a)) # will not throw an error
