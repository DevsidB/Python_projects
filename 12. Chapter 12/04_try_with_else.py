'''In Try with else statement we get the output in else only after the code was sucessfully executed.
While in a loop using a try catch doesn't crash the code. Without try else the code in the loop crashes for 
any kind of errors'''

# while True: 
#     try:
#         i = int(input("Enter a number: "))
#         c = 1/i
#     except Exception as e:
#         print(e)
#     else: ## to excecute only if the try was successful. 
#         print("We were successful")

'''Here the code will crash for wrong input values that can cause an error.'''
# while True:     
#     i = int(input("Enter a number: "))
#     c = 1/i
#     print("We were successful")


'''Try except else and finally'''
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit() ##Exit the code

else: ## to excecute only if the try was successful. 
    print("We were successful")

finally: ## To execute the code even if the try code was unsuccessful and was exited in the except clause. 
    print("We are done")

print("Thanks for using the program") # This line will not print if code was exited. But will print if the exit command is not used inside except.