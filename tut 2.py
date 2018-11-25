Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> pet=input('No of Pets You have :\n')
No of Pets You have :
5
>>> print('You have ',pet ,'Pets')
You have  5 Pets
>>> print('You have',pet ,'Pets')
You have 5 Pets
>>> 


>>> 

>>> 


>>> 


>>> 


>>> 

>>> 



>>> 

>>> 


>>> 


>>> 


>>> 

>>> 


>>> 


>>> 


>>> 


>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 



>>> 

>>> 



>>> 

>>> 


>>> 


>>> 


>>> 


>>> 


>>> total =0
>>> total = total +5
>>> print(total)
5
>>> total = total +8
>>>  print(total)
SyntaxError: unexpected indent
>>>  print(total)
SyntaxError: unexpected indent
>>> 
>>> 
>>> total =0
>>> total = total +5
>>> print(total)
5
>>> total = total +8
>>> print(total)
13
>>> total = total +2
>>> print(total)
15
>>> total = total +3
>>> print(total)
18
>>> 
>>> 
>>> total = 0
>>> num1 =input('Enter a Number:\n')
Enter a Number:
45
>>> num2 =input('Enter a Number:\n')
Enter a Number:
59
>>> total =  num1 + num2
>>> print(total)
4559
>>> total= int(num1) + int(num2)
>>> print(total)
104
>>> 
>>> cost = input('Cost of Item')
Cost of Item
>>> 
>>> 
>>> 
>>> cost = input('Cost of Item :\n')
Cost of Item :
Cost of Item :
>>> 
>>> cost = input('Cost of Item : ')
Cost of Item : 156
>>> cash = input('Cash Paid : ')
Cash Paid : 800
>>> change = int(cash) - int(cost)
>>> print(change)
644
>>> 
>>> 
>>> num1 = input('Input First Number : \n')
Input First Number : 
85
>>> num2 = input('Input Second Number : \n')
Input Second Number : 
78
>>> num3 = input('Input Third Number : \n')
Input Third Number : 
23
>>> Total = int(num1 + num2 +num3)
>>> Average = Total/3
>>> print(Average)
285941.0
>>> print(Total)
857823
>>> Total = int(num1) +  int(num2) +int(num3)
>>> Average = Total/3
>>> print(Total)
186
>>> print(Average)
62.0
>>> centigrade = input int('Enter Centigrade temperature (c) : \n')
SyntaxError: invalid syntax
>>> centigrade = input(int('Enter Centigrade temperature (c) : \n'))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    centigrade = input(int('Enter Centigrade temperature (c) : \n'))
ValueError: invalid literal for int() with base 10: 'Enter Centigrade temperature (c) : \n'
>>> int(centigrade) = input('Enter Centigrade temperature (c) : \n')
SyntaxError: can't assign to function call
>>> 
>>> 
>>> 
>>> 
>>> 
>>> centigrade = input('Enter Centigrade temperature (c) : \n')
Enter Centigrade temperature (c) : 
Enter Centigrade temperature (c) :

>>> centigrade = input('Enter Centigrade temperature (c) : ')
Enter Centigrade temperature (c) : 100
>>> centigrade = int(c)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    centigrade = int(c)
NameError: name 'c' is not defined
>>> 
>>> 
>>> 
>>> centigrade
'100'
>>> 

>>> centigrade = input('Enter Centigrade temperature (c) : ')
Enter Centigrade temperature (c) : 100
>>> f = (9/5)*int(centigrade) + 32
>>> print(f)
212.0
>>> 

>>> 
>>> centigrade = input('Enter Centigrade temperature (c) : ')
Enter Centigrade temperature (c) : 100

>>> c= int(centigrade)
>>> f = (9/5)*c + 32
>>> Fahrenheit = int(f)
>>> print(Fahrenheit)
212
>>> # here only for integer value#
>>> centigrade = input('Enter Centigrade temperature (c) : ')
Enter Centigrade temperature (c) : 45

>>> c= int(centigrade)
>>> f = (9/5)*c + 32
>>> Fahrenheit = int(f)
>>> print(Fahrenheit)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> centigrade = input('Enter Centigrade temperature (c) : ')
Enter Centigrade temperature (c) : 45
>>> c= int(centigrade)
>>> f = (9/5)*c + 32
>>> Fahrenheit = int(f)
>>>  print(Fahrenheit)
SyntaxError: unexpected indent
>>> print(Fahrenheit)
113
>>> centigrade = input('Enter Centigrade temperature (c) : ')

Enter Centigrade temperature (c) : 56
>>> c= int(centigrade)
>>> f = (9/5)*c + 32
>>> Fahrenheit = int(f)
>>> print(Fahrenheit)
132
>>> # actual answer is 132.8 but fractional part ignored#bcz int()
>>> 

>>> 
>>> 
>>> Length = input("Enter the Length of the Box : ")
Enter the Length of the Box : 63
>>> Height = input("Enter the Height of the Box : ")
Enter the Height of the Box : 89
>>> Width = input("Enter the Width of the Box : ")
Enter the Width of the Box : 32
>>> L = int(Length)
>>> H = int(Height)
>>> W = int(Width)
>>> Volume = L*H*W
>>> print(Volume)
179424
>>> 
>>> 
>>> Meters = input("Enter No of Meters : ")
Enter No of Meters : 5
>>> M = int(Meters)
>>> c = 100* M
>>> c = int(Centimeters)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    c = int(Centimeters)
NameError: name 'Centimeters' is not defined
>>> Centimeters = int(c)
>>> print(Centimeters)
500
>>> 
