## using append command
# for i in range (2,21):
#     for j in range (1,11):
#         with open (f"tables/Multiplication table of {i}.txt","a") as f: ##remember to take append else the last 
# range will keep ovewriting the text i.e only 2x10 will be printed in the text.One the loop is completed the file
# closes and write command will only overwrite the complete data once file is opened again.
#             f.write (f"{i}x{j}= {i*j}\n")

# ## using write conmmand
# for i in range (2,21):
#     with open (f"tables/Multiplication table of {i}.txt","w") as f: 
#         for j in range (1,11):  ## keeping for loop inside open enables us to use write command without using append as it keeps the file
#                                 #open and keeps printing the data contained in the loop without closing it.
#             f.write (f"{i}x{j}= {i*j}\n")

## using write command with break to print a single table just for checking the loop 
for i in range (2,21):
    with open (f"tables/Multiplication table of {i}.txt","w") as f: 
        for j in range (1,11):  ## keeping for loop inside open enables us to use write command without using append as it keeps the file
                                #open and keeps printing the data contained in the loop without closing it.
            f.write (f"{i}x{j}= {i*j}") # \n inside the string will add an extra line after 2x10
            if j!= 10:   ## removes the extra line printed after 2x10 on the 11th line in notepad.
                f.write("\n")
    break  ## if break is removed all the tables will be printed.
