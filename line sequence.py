'''
Write a Python program that accepts a sequence of lines (blank line to terminate)
as input and prints the lines as output (all characters in lower case).
'''
l=[]
while True:
    a=input()
    if a:
        l.append(a.upper())
    else:
        break
for a in l:
    print(a)