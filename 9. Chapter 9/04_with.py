# with open ("another.txt", 'r') as f:
#     a= f.read(10)
#     print (a)

with open ("another.txt", 'w') as f: ## with statement automatically closes the file. No need to write a fn to close the file.
    a= f.write("me")
print (a)

# with open ("another.txt", 'w') as f: ## with statement automatically closes the file. No need to write a fn to close the file.
#     a= f.write("me")
#     a= f.write("you")
#     a= f.write("together")
#     a= f.write("foreva")
# print (a)