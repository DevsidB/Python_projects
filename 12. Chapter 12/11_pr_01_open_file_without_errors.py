# # method 1
# try:
#     print ("    Opening file ...")
#     with open ("3.txt", "r") as f:
#         a= f.read()
#         print(a)
#         print("*****File opened successfully*****")
# except:
#     print ("The file doesn't exist. Try entering a different name.")
# print ("The code 1 executed \n")

# try:
#     print ("    Opening file ...")
#     with open ("2.txt", "r") as f:
#         a= f.read()
#         print(a)
#         print("*****File opened successfully*****")
# except:
#     print ("The file doesn't exist. Try entering a different name.")
# print ("The code 2 executed \n")

# try:
#     print ("    Opening file ...")
#     with open ("1.txt", "r") as f:
#         a= f.read()
#         print(a)
#         print("*****File opened successfully*****")
# except:
#     print ("The file doesn't exist. Try entering a different name.")
# print ("The code 3 executed \n")

# Method 2 - Using a function to minimize the code repeatability.
def fileOpen(filename):
    try:
        print ("    Opening file ...")
        with open (filename , "r") as f:
            a= f.read()
            print(a)
            print(f"*****File {filename} opened successfully*****")
    except:
        print (f"The file {filename} doesn't exist. Try entering a different name.")
    print ("The code executed \n")

fileOpen("1.txt")
fileOpen("2.txt")
fileOpen("3.txt")