#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#Vrushabh Amrutiya 20CS004
lst=['red','red','red','red','yellow','blue','black','white']
tpl=(2,2,3,3,3,4,5,6)
dct = {'a':100, 'b':100, 'c':200, 'd':250}
print(max(set(lst),key=lst.count))
print(max(set(tpl),key=tpl.count))
max(dct.iterkeys(), key = dct.get)