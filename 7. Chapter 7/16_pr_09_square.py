## my method to print the user entered square:
n=int(input("enter number:"))
print ("*" * n)
c= n-2
for i in range (c):
    print ("*" + " "*c + "*")
print ("*" * n)



# ## some youtube user method : not working 
# n=int(input("enter number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==2 and j==2:
#             print(" ",end="")
#             continue
#         elif i==2 and j==3:
#             print(" ",end="")
#             continue
#         elif i==2 and j==4:
#             print(" ",end="")
#             continue
#         elif i==3 and j==2:
#             print(" ",end="")
#             continue
#         elif i==3 and j==3:
#             print(" ",end="")
#             continue
#         elif i==3 and j==4:
#             print(" ",end="")
#             continue
#         elif i==4 and j==2:
#             print(" ",end="")
#             continue
#         elif i==4 and j==3:
#             print(" ",end="")
#             continue
#         elif i==4 and j==4:
#             print(" ",end="")
#             continue
#         print("*",end="")
#     print("")