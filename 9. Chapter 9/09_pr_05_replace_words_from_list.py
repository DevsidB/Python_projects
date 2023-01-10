words= ["donkey", "mota", "gadha"]

with open ("abusive.txt") as f:
    f= f.read()
    data= f.lower()
print (data)

with open ("abusive.txt", 'w')as f :
    for word in words:
        data= data.replace(word, "##$%^#@%")
        data = data.capitalize()
    f.write(data)
    
print (data)   
