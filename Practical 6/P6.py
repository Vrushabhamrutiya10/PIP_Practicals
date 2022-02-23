# 20CS004 Vrushabh Amrutiya
# AIM
# You are given n words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# REPOSITORY LINK:
# https://github.com/Vrushabhamrutiya10/PIP_Practicals

from collections import Counter
# take input or number of words.
x = int(input())
lst = []
# appending the words in the list.
for i in range(x):
    lst.append(input().strip())
# count the number of times each element appears.
ct = Counter(lst)
# printing the no of counts (no of distinct words) 
# and how many times each word appears.
print(len(ct))
print(*ct.values())