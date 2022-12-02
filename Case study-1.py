#Case study-1
#1
l = [x*x for x in range(0,10)]
print(l)
#2
year = int(input("Enter the year :"))

a = "The entered year is Leap Year"
b = "The entered year is not leap year"
if year % 100 == 0 and year % 400 == 0: 
    print(a)
elif year % 4==0:
    print(a)
else:
       print(b)
 
 #3
array = [1,2,3,4,5,6] 
 
def even(array): 
	new_array = [] 
	for i in array: 
		if i%2==0: 
			new_array.append(i) 
	return new_array 
 
print(even(array)) 
#4
array1 = [1,2,3,4,5,6,7,8,9,10]
array2 = [4,6,7,9,]
for array1 in array2:
    print(array1)



       
