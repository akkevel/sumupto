# Write a program that asks for a positive integer and outputs the sume of all numbers between one and that number
print('This little program will sum all the number between 0 and the number you enter')
x = int(input("Please enter a positive integer: "))

if x < 0:
    print('this is a negative number, please give a POSITIVE integer')
elif x == 0:
    print('there are no numbers between 0 and 0, so no summing done')
else:
    i = range (x)
    b = sum(i)
    print(b, 'is the sum of all numbers between 0 and', x)
