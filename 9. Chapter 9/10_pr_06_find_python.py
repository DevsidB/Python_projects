with open ("log.txt", 'r') as f:
    content= f.read().lower()

if 'python' in content:
    print (True)
else:
    print (False)
