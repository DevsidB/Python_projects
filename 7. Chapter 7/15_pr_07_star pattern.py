n= int(input(" enter the number: "))
count = 1
space= (n-1)
for i in range (1,n+1):
    print (" " * space + "*" * count)
    count = count + 2
    space= space-1

# ##sankets diamond program 10 mark   - 12344321  
# n= int(input(" enter the number: "))
# count = 1
# space= (n-1)
# for i in range (1,n+1):
#     print (" " * space + "*" * count)
#     count = count + 2
#     space= space-1

# count= ((n-1)*2)-1
# space= 1
# for i in range (1,n):
#     print (" " * space + "*" * count)
#     count = count-2
#     space= space+1
##---------------------------------------------
##else - no double centre line 1234321

# count= (n*2)-1
# space= 0
# for i in range (1,n):
#     print (" " * space + "*" * count)
#     count = count-2
#     space= space+1
##-----------------------------------------------
