# 20CS004 Vrushabh Amrutiya
# AIM
# Lapindrome is defined as a string which when split in the middle,
# gives two halves having the same characters and same frequency of each character.
# If there are odd number of characters in the string, we ignore the middle character
# and check for lapindrome. For example gaga is a lapindrome, since the two halves
# ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy
# are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves
# contain the same characters but their frequencies do not match. Your task is simple.
# Given a string, you need to tell if it is a lapindrome.
# REPOSITORY LINK:
# https://github.com/Vrushabhamrutiya10/PIP_Practicals

#input the number of words.
v = int(input())
# input the word
for i in range(v):
    word = input()
    #divding the word into 2 parts a and b by length (even and odd)
    l = len(word)
    if l % 2 == 0:
        x = word[:l//2]
        y = word[l//2:]
    else:
        x = word[:l//2]
        y = word[l//2+1:]
    # printing the result if or not the word is a lapindrome
    if sorted(x) == sorted(y):
        print("YES")
    else:
        print("NO")