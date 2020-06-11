'''
Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''
c=int(input('enter celcius: '))
f=(9*c)//5+(32)
print(c,'celcius is {} in fahrenheit'.format(f))
f=int(input('enter fahrenheit: '))
c=(5*(f-32))//9
print(f,'fahrenheit is {} in fahrenheit'.format(c))