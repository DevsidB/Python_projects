name = input ('enter the name to check in the database: \n')
nlist= ['sanket','ajay','sid']
if (name in nlist):
    print ("the name '"+ name + "' you entered is available in the dataset")
else :
    print ("the name '"+ name + "' you entered is not available in the dataset")