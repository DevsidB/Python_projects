text= input ('enter the text: \n')
spam = False
if ("make a lot of money"in text):
    spam = True
elif("buy now"in text):
    spam = True
elif ("subscribe this"in text):
    spam = True
elif ("click this"in text):
    spam = True
if (spam):
    print ("This text is a spam")
else :
    print ('This text is not a spam')
