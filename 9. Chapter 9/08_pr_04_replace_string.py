# with open ("abusive.txt", 'r') as f:
#     data = f.read()
#     print (data)

# f= open("abusive.txt",'r')  ## Returns in text "r"
# data= f.read() # will return only first 10 strings.
# print (data)
# f.close()

with open ("abusive.txt", 'r') as f:
    f=f.read()
    data = f.lower()
    data= data.replace("donkey", "######")
    data= data.replace("bitch", "######")
    data= data.capitalize()
print (data)

with open ("abusive.txt", 'w') as f:
   f= f.write(data)