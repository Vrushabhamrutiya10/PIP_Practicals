#c. Write a Python program to sum all the items in a dictionary.
#Vrushabh Amrutiya 20CS004
dct = {'a':100, 'b':150, 'c':200, 'd':250}
#add values of all the elements
sum=0
for i in dct.values():
    sum=sum+i

print(sum)