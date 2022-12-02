#Assignment 1
a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

#Assignment 2

a = int(input("Enter first number :"))
b= int(input("Enter second number :"))
c=  int(input("Enter third number :"))

if a>=b and a>=c:
    largest = a
elif b>=a and b>=c:
       largest = b
else:
    largest = c
print("The greatest number is", largest)
