'''
Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
c,d=0,0
for i in numbers:
    if i%2==0:
        c+=1
    else:
        d+=1
print(c,d)