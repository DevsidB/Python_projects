num = int(input("Enter your number: "))

table = [num*i for i in range(1, 11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table))
    # f.write(table) # Type error. write argument need to be in a str format not list. This will not append
    f.write('\n')