## completely overwrites the text in the file if file is present else creates a new file with the given name.

## Write Function - Open the file and then use w in the syntax and use write function 
# 1. Open the file and then 
# 2. use 'w' in the syntax and 
# 3.use write function 
f= open("another.txt","w" )
f.write("This is over written by Me.\n ")
f.close()

# ## Write Function - 
# 1. Open the file and then 
# 2. use 'a' in the syntax and 
# 3.use write function 
f= open("another.txt","w" )
f.write("This is also over written by Me.\n ")
f.close()

f= open("another.txt","w" )
f.write("This is also over written by Me for third time. ")
f.close()