i = 1
with open ("log.txt") as f:
    while 1==1:
        data = f.readline().lower()
        if 'python' in data:
            print (f"The word you are looking for is on line number {i}")
        i = i+1
        #i+=1 # Alternartive to i = i+1