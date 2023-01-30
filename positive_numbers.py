#author : Lakshmi A G
#30 Jan 2023
#Write a Python program to print all positive numbers in a range.

list1 = eval(input("Enter the list :"))
for i in list1:
    if (i > 0):
        print (i, end =",")
