num=int(input("Enter The Number to print the table :"))

for x in range(1,11):
    print(num," x ",x," = ", num*x)

total =0
for y in range(5):
    numb = int(input("Enter a Number : "))
    total = total+numb
    
print("The total is : ",total)


for num in range(0,50):
    if num%2==1:
        print(num)
    else:
        continue 


str=int(input("Enter The Number to print the Star :"))
for num in range(str):
    print("*",end="") 


import random
count=0
for x in range(100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    if dice1==dice2:
        count+=1
    else:
        continue
print("Out of 100 you rolled ",count,"doubles") 


for number in range(3):
    print("------------------------------------------")
    print("Outer loopiteration "+str(number))
    #inner loop
    for another_number in range(4):
        print("********************************************")
        print("In inner loop iteration " + str(another_number))


for x in range(1,4):
    for y in range(1,4):
        print("*",end="")
    print()


for x in range(1,4):
    for y in range(1,x+1):
        print("*",end="")
    print()


n = input("Please enter an Integer :")
try:
    n=int(n)
except ValueError:
    print("Requires a valid Integer !")


while True:
    n=input("Please enter an Integer :")
    try:
        n=int(n)
        break
    except ValueError:
        print("Requires a valid Integer ! Please Try Again ")
print("You successfully entered an Integer") """


try:
    x=2/0
except ZeroDivisionError:
    print("Cannot Devide by Zero ")
    
          
    


        
