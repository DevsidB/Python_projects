
# print (open ("sample.txt", 'r').read())
# open ("sample.txt", 'r').close()

f= open("sample.txt",'r')  ## Returns in text "r"
data= f.read(10) # will return only first 10 strings.
print (data)
f.close()

f= open("sample.txt",'rb')   ## Returns in binary "rb"
data= f.read()
print (data)
f.close()