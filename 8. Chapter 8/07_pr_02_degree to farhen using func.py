
def conv(degree):
    return (degree * 9/5) + 32
while True :
    value = int(input("Enter the value to convert to farenheit: "))
    print ("Your Entered Value converted to farenheit is :",conv(value))
