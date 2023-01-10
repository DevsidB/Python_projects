# ## My method to remove a word from a string and strip it
# text = "          Language Python is a fun language to Learn             "

# def remove_strip(string, word):
#     return (string.replace(word, "")).strip()

# print (remove_strip(text,"Language"))

# #-------------------------------------------------------------------------------------------

# Another method to remove a word from a string and strip it(Variables used rest is same)
text = "          Language Python is a fun language to Learn             "

def remove_strip(string, word):
    a= string.replace(word, "")
    return a.strip()
b=remove_strip(text,"language ")
print (b)

