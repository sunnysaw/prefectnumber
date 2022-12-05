"""In this section we are given a question by our college teacher, and we have to solve that question:
_____________________________________________________________________________________________________
Question : Write a python program to find largest among three number:
_________________________________________________________________________
Approach : first we take input from user, and then we will compare three number with each other and then print that output:
"""
a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))
if(a > b):
    print("number a is greater than b" , a)
elif(a > c):
    print("number a is greater than a", a)
elif(b > a):
    print("number a is greater than b", b)
elif(b > a):
    print("number a is greater than b", b)
elif(c > a):
    print("number a is greater than c", c)
elif(c > b):
    print("number a is greater than c", c)
else:
    print("number enter by user in incorrect")