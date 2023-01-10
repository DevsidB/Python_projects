# i=2
# j=3
# for i in range (0,5) :
#     if i == 2 and j == 3:
#         print ("catch")
#         continue
#     print (i)
#     print ("done")
# else:
#     print ("value not found")

n=int(input("enter number:"))
print ("*" * n)
c= n-2
for i in range (c):
    print ("*" + " "*c + "*")
print (f"*" * n)