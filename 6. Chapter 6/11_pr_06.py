# to return yes or no if a string is available in the user entered text
text = "HArRyhadalittleLaMb"
text=text.lower()
print (text)
usertext= input ("Enter text you want to search: \n")

if usertext in text :
    print ("yes")
else :
    print ("no")
