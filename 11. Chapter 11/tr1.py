vec=[2,4,6]
str=""
index=0
for i in vec:
    str= str + f"{i}a{index} + "  
    index +=1
str= str[:-3]
print (str)