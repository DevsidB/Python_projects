def greet(name):
    print(f"Good morning, {name}")

# print(__name__) #Name of file is __main__ by default for the current file.
if __name__ == "__main__": # Only if the function is called from the current file, the next lines of code will be executed.
    n = input("Enter a name\n")
    greet(n)
