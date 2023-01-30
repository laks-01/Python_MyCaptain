#author : Lakshmi A G
#30 Jan 2023
#Fibonacci numbers

num = int(input("Enter the range :"))
num1 = 0
num2 = 1
print (num1)
print (num2)
for i in range (1,num):
    num3 = num1+num2
    print(num3)
    num1 = num2
    num2 = num3
