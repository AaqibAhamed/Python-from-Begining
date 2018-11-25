score=-9
count=1
guesn=[]
total=0

guser =int(input("Enter a Number : "))
guesn.append(guser)
while True:
    if guser!=score:
        guser=int(input("Enter a Number again : "))
        guesn.append(guser)
        count+=1
        continue
    else:
        break
for x in guesn:
    total=total+x
print("Average of the numbers: ",total/count)
