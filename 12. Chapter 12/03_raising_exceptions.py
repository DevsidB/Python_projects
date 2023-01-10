# def increment(num):
#     try:
#         return int(num) + 1
#     except:
#         raise ZeroDivisionError("This is not good caused a zero div err - Harry")

# a = increment('df364')
# print(a)

def increment(num):
    try:
        return 10/int(num)
    except: ## only one error can be handled. Overwrites the default error message. 
        raise ZeroDivisionError ("This is not good - Harry") #Only one type of error mentioned here will be displayed along with the custom message for whatsover type of error caused by error. 

    # except: ## only one catch all except clause allowed.cannot add other error message.
    #  
    #     raise ZeroDivisionError ("This is not good - Harry")

# a= increment(3)
a = increment('gfdg') # Even when a string is given as input, zero divsion error will be displayed because of overwriting the error. 
print(a)