# # program to greet only the people whose names starts with "s": My method
# l1 = ["harry", "soham", "sachin", "rahul"]
# for i in range (4):
#     index = l1[i]
#     if index.startswith("s") is True:
#         print (f"Welcome to Goa {l1[i]}")



# # info : printing every word in the list
# l1 = ["harry", "soham", "sachin", "rahul"]
# for i in l1: # i can be replaced with any variable name eg: for name in l1/ for friends in l1/ for a in l1 etc
#     print (i)


# # program to greet only the people whose names starts with "s": Harry's  method
l1 = ["harry", "soham", "sachin","sanket","sid","rahul"]
for name in l1: # i can be replaced with any variable name eg: for name in l1/ for friends in l1/ for a in l1 etc
    if name.startswith("s"):
        print ("hello " + name)
