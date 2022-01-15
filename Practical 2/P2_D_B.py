#b. Write a Python script to merge two Python dictionaries.
#Vrushabh Amrutiya 20CS004
dct = {'0':'red', '1':'blue', '2':'white', '3':'black'}
dct2={'a':'apple','b':'melon','c':'cherry','d':'grapes'}
def Merge(dct, dct2):
    return(dct2.update(dct))
#update() function will upate a dict by adding all the elements
Merge(dct, dct2)
print(dct2)