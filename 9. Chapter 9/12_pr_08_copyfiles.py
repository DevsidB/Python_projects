with open ("this.txt") as f:
    data= f.read()

with open ("this2.txt", 'w') as f:
    data2= f.write(data)
