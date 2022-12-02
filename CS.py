#if,else,elif
x = 20

if x < 20:
    print("X is less than 20")
elif x == 20:
    print("X is equal to 20")
else:
    print("X is greater than 20")
    
#nested if-else
x=16
if x < 20:
    print("X is less than 20")
    if x < 15:
        print("X is less than 15")
    else:
        print("X is greater than 15")
else:
    print("X is greather than 20") 

